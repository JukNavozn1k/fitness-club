from abc import ABC, abstractmethod
from sqlalchemy.future import select
from sqlalchemy import inspect, update, delete
from sqlalchemy.orm import class_mapper, Load, RelationshipProperty
from typing import List, Dict, Optional, Any

from beanie import Document,Link
from typing import Type

class AbstractRepository(ABC):
    @abstractmethod
    async def create(self, data: Dict) -> Dict:
        raise NotImplementedError

    @abstractmethod
    async def retrieve(self, pk: int) -> Optional[Dict]:
        raise NotImplementedError

    @abstractmethod
    async def retrieve_by_field(self, field_name: str, value: Any) -> Optional[Dict]:
        raise NotImplementedError

    @abstractmethod
    async def list(self) -> List[Dict]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, pk: int, data: Dict) -> Optional[Dict]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, pk: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def create_many(self, data_list: List[Dict]) -> List[Dict]:
        raise NotImplementedError

    @abstractmethod
    async def retrieve_by_field(self, field_name: str, value: Any) -> Optional[Dict]:
        raise NotImplementedError

    @abstractmethod
    async def update_many(self, filters: Dict, update_data: Dict) -> int:
        raise NotImplementedError

    @abstractmethod
    async def delete_many(self, filters: Dict) -> int:
        raise NotImplementedError

class AbstractSQLRepository(AbstractRepository, ABC):
    def __init__(self, get_session, model):
        self.get_session = get_session
        self.model = model

    def _to_dict(self, instance, visited=None):
        if visited is None:
            visited = set()

        result = {
            column.key: getattr(instance, column.key)
            for column in class_mapper(instance.__class__).columns
        }

        state = inspect(instance)

        for name, relation in class_mapper(instance.__class__).relationships.items():
            if relation not in visited:
                visited.add(relation)

                if name in state.unloaded:
                    fk_value = getattr(instance, f"{name}_id", None)
                    if fk_value is not None:
                        result[f"{name}_id"] = fk_value
                else:
                    related_obj = getattr(instance, name)
                    if related_obj is not None:
                        if relation.uselist:
                            result[name] = [
                                self._to_dict(child, visited) for child in related_obj
                            ]
                        else:
                            result[name] = self._to_dict(related_obj, visited)
        return result

    def _prepare_instance(self, data: Dict):
        instance = self.model(**{k: v for k, v in data.items() if not isinstance(v, (dict, list))})
        for field, value in data.items():
            if hasattr(self.model, field) and isinstance(getattr(self.model, field).property, RelationshipProperty):
                related_model = getattr(self.model, field).property.mapper.class_
                if isinstance(value, list):
                    related_instances = [related_model(**item) for item in value]
                    setattr(instance, field, related_instances)
                else:
                    related_instance = related_model(**value)
                    setattr(instance, field, related_instance)
        return instance

    async def create(self, data: Dict) -> Dict:
        async with self.get_session() as session: 
            instance = self._prepare_instance(data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return self._to_dict(instance)
    
    async def create_many(self, data_list: List[Dict]) -> List[Dict]:
        async with self.get_session() as session:
            instances = [self._prepare_instance(data) for data in data_list]
            session.add_all(instances)
            await session.commit()
            for instance in instances:
                await session.refresh(instance)
            return [self._to_dict(instance) for instance in instances]
        
    async def retrieve_by_field(self, field_name: str, value: Any, options: Optional[List[Load]] = None) -> Optional[Dict]:
        async with self.get_session() as session:
            query = select(self.model).filter(getattr(self.model, field_name) == value)
            if options:
                query = query.options(*options)
            result = await session.execute(query)
            instance = result.scalar_one_or_none()
            return self._to_dict(instance) if instance else None
    
    async def retrieve(self, pk: int, options: Optional[List[Load]] = None) -> Optional[Dict]:
        return await self.retrieve_by_field("id", pk, options)

    async def list(self, options: Optional[List[Load]] = None, filters: Optional[Dict[str, Any]] = None) -> List[Dict]:
        async with self.get_session() as session:
            query = select(self.model)
            if filters:
                query = query.filter_by(**filters)
            if options:
                query = query.options(*options)
            result = await session.execute(query)
            return [self._to_dict(instance) for instance in result.scalars().all()]

    async def update(self, pk: int, data: Dict) -> Optional[Dict]:
        async with self.get_session() as session:
            result = await session.execute(select(self.model).filter_by(id=pk))
            instance = result.scalar_one_or_none()
            if instance:
                for key, value in data.items():
                    if hasattr(self.model, key) and isinstance(getattr(self.model, key).property, RelationshipProperty):
                        related_model = getattr(self.model, key).property.mapper.class_
                        if isinstance(value, list):
                            related_instances = [related_model(**item) for item in value]
                            setattr(instance, key, related_instances)
                        else:
                            related_instance = related_model(**value)
                            setattr(instance, key, related_instance)
                    else:
                        setattr(instance, key, value)
                await session.commit()
                await session.refresh(instance)
                return self._to_dict(instance)
            return None

    async def update_many(self, filters: Dict, update_data: Dict) -> int:
        async with self.get_session() as session:
            stmt = update(self.model).filter_by(**filters).values(**update_data)
            result = await session.execute(stmt)
            await session.commit()
            return result.rowcount

    async def delete(self, pk: int) -> bool:
        async with self.get_session() as session:
            result = await session.execute(select(self.model).filter_by(id=pk))
            instance = result.scalar_one_or_none()
            if instance:
                await session.delete(instance)
                await session.commit()
                return True
            return False

    async def delete_many(self, filters: Dict) -> int:
        async with self.get_session() as session:
            stmt = delete(self.model).filter_by(**filters)
            result = await session.execute(stmt)
            await session.commit()
            return result.rowcount
        


class AbstractMongoRepository(ABC):
    """
    Абстрактный репозиторий для MongoDB на базе Beanie с поддержкой Link-сущностей.
    Ожидается, что self.model является подклассом beanie.Document.
    """
    def __init__(self, model: Type[Document]):
        self.model = model

    async def _prepare_data_with_links(self, data: Dict) -> Dict:
        """
        Обрабатывает данные перед созданием документа:
        Если какое-либо поле модели является Link и в data передан словарь,
        то создаётся соответствующий связанный документ.
        """
        # Обходим все поля, определённые в модели (используем pydantic-свойства)
        for field, field_info in self.model.__fields__.items():
            if field in data and isinstance(data[field], dict):
                # Проверяем, является ли тип поля Link[...] (generic)
                field_type = field_info.outer_type_
                if hasattr(field_type, '__origin__') and field_type.__origin__ is Link:
                    # Получаем класс связанного документа из параметров generic
                    linked_model = field_type.__args__[0]
                    # Создаем экземпляр связанного документа
                    linked_instance = linked_model(**data[field])
                    await linked_instance.insert()  # сохраняем связанный документ
                    data[field] = linked_instance  # подставляем готовый объект вместо dict
        return data

    async def create(self, data: Dict) -> Dict:
        """
        Создание одной сущности с поддержкой Link-сущностей.
        """
        data = await self._prepare_data_with_links(data)
        document = self.model(**data)
        await document.insert()
        return document.model_dump()

    async def create_many(self, data_list: List[Dict]) -> List[Dict]:
        """
        Создание множества сущностей с поддержкой Link-сущностей.
        Обрабатываем каждую запись отдельно.
        """
        prepared_data_list = []
        for data in data_list:
            prepared_data = await self._prepare_data_with_links(data)
            prepared_data_list.append(prepared_data)
        documents = [self.model(**data) for data in prepared_data_list]
        await self.model.insert_many(documents)
        return [doc.model_dump() for doc in documents]

    async def _populate_field(self, document: Document, field_path: str) -> None:
        """
        Рекурсивное заполнение связанной сущности по заданному пути (например, "profile.test").
        Для каждого уровня, если поле является ссылкой (Link), вызывается fetch_link.
        """
        parts = field_path.split('.')
        current_obj = document
        for part in parts:
            if hasattr(current_obj, 'fetch_link'):
                field_ref = getattr(current_obj, part, None)
                if field_ref is not None:
                    await current_obj.fetch_link(field_ref)
            current_obj = getattr(current_obj, part, None)
            if current_obj is None:
                break

    async def _populate_document(self, document: Document, populate: List[str]) -> None:
        """
        Заполняет все указанные поля для документа, поддерживая вложенные пути.
        """
        for field in populate:
            await self._populate_field(document, field)

    async def retrieve(self, pk: Any, populate: Optional[List[str]] = None) -> Optional[Dict]:
        """
        Получение одной сущности по первичному ключу.
        Если передан populate, заполняет связанные Link-сущности.
        """
        document = await self.model.get(pk)
        if document and populate:
            await self._populate_document(document, populate)
        return document.model_dump() if document else None

    async def retrieve_by_field(self, field_name: str, value: Any, populate: Optional[List[str]] = None) -> Optional[Dict]:
        """
        Получение одной сущности по значению произвольного поля.
        """
        document = await self.model.find_one({field_name: value})
        if document and populate:
            await self._populate_document(document, populate)
        return document.model_dump() if document else None

    async def list(self, filters: Optional[Dict] = None, populate: Optional[List[str]] = None) -> List[Dict]:
        """
        Получение списка сущностей с возможностью фильтрации.
        """
        filters = filters or {}
        cursor = self.model.find(filters)
        documents = await cursor.to_list()
        if populate:
            for doc in documents:
                await self._populate_document(doc, populate)
        return [doc.model_dump() for doc in documents]

    async def update(self, pk: Any, data: Dict, populate: Optional[List[str]] = None) -> Optional[Dict]:
        """
        Обновление сущности по первичному ключу с поддержкой Link-сущностей.
        Если для Link-поля передается словарь, создаётся новый связанный документ.
        """
        document = await self.model.get(pk)
        if not document:
            return None

        # Если в данных есть Link-поля, обрабатываем их отдельно
        data = await self._prepare_data_with_links(data)

        for key, value in data.items():
            setattr(document, key, value)
        await document.save()
        if populate:
            await self._populate_document(document, populate)
        return document.model_dump()

    async def update_many(self, filters: Dict, update_data: Dict) -> int:
        """
        Массовое обновление сущностей по фильтру.
        Используется оператор "$set" для обновления.
        В update_many не обрабатываем вложенные Link-сущности, так как они обновляются отдельно.
        """
        update_result = await self.model.find(filters).update({"$set": update_data})
        return update_result.modified_count

    async def delete(self, pk: Any) -> bool:
        """
        Удаление одной сущности по первичному ключу.
        """
        document = await self.model.get(pk)
        if document:
            await document.delete()
            return True
        return False

    async def delete_many(self, filters: Dict) -> int:
        """
        Массовое удаление сущностей по фильтру.
        """
        delete_result = await self.model.find(filters).delete()
        return delete_result.deleted_count