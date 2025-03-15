from abc import ABC, abstractmethod
from sqlalchemy.future import select
from sqlalchemy import inspect
from sqlalchemy.orm import class_mapper,Load
from typing import List, Dict, Optional, Any


class AbstractRepository(ABC):
    @abstractmethod
    async def create(self, data: Dict) -> Dict:
        raise NotImplementedError

    @abstractmethod
    async def create_many(self, data_list: List[Dict]) -> List[Dict]:
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
    async def delete_many(self, ids: List[int]) -> bool:
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

    async def create(self, data: Dict) -> Dict:
        async with self.get_session() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            return self._to_dict(instance)

    async def create_many(self, data_list: List[Dict]) -> List[Dict]:
        async with self.get_session() as session:
            instances = [self.model(**data) for data in data_list]
            session.add_all(instances)
            await session.commit()
            return [self._to_dict(instance) for instance in instances]
        
    async def retrieve_by_field(self, field_name: str, value: Any, options: Optional[List[Load]] = None, filters: Optional[Dict[str, Any]] = None) -> Optional[Dict]:
        async with self.get_session() as session:
            query = select(self.model).filter(getattr(self.model, field_name) == value)
            if filters: 
                query = query.filter_by(**filters)
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
                    setattr(instance, key, value)
                await session.commit()
                return self._to_dict(instance)
            return None

    async def delete(self, pk: int) -> bool:
        async with self.get_session() as session:
            result = await session.execute(select(self.model).filter_by(id=pk))
            instance = result.scalar_one_or_none()
            if instance:
                await session.delete(instance)
                await session.commit()
                return True
            return False

    async def delete_many(self, ids: List[int]) -> bool:
        async with self.get_session() as session:
            result = await session.execute(select(self.model).filter(self.model.id.in_(ids)))
            instances = result.scalars().all()
            if instances:
                for instance in instances:
                    await session.delete(instance)
                await session.commit()
                return True
            return False
        
    async def get_attribute(self, pk: int, attr_name: str) -> Any:
        """Получает значение атрибута модели, включая отношения."""
        async with self.get_session() as session:
            result = await session.execute(select(self.model).filter_by(id=pk))
            instance = result.scalar_one_or_none()
            if not instance:
                return None

            attr_value = getattr(instance, attr_name, None)
            if isinstance(attr_value, list):  # Если это список объектов
                return [self._to_dict(obj) for obj in attr_value]
            return attr_value  # Возвращаем обычное значение

    async def set_attribute(self, pk: int, attr_name: str, value: Any) -> Optional[Dict]:
        """Устанавливает значение атрибута модели, включая отношения."""
        async with self.get_session() as session:
            result = await session.execute(select(self.model).filter_by(id=pk))
            instance = result.scalar_one_or_none()
            if not instance:
                return None

            if attr_name in class_mapper(self.model).relationships:
                # Обновление отношения (если передан список ID)
                relation = class_mapper(self.model).relationships[attr_name]
                related_model = relation.mapper.class_

                # Удаляем старые связи
                current_relations = getattr(instance, attr_name)
                for rel_obj in current_relations:
                    await session.delete(rel_obj)

                # Добавляем новые связи
                new_objects = await session.execute(select(related_model).filter(related_model.id.in_(value)))
                new_objects = new_objects.scalars().all()
                setattr(instance, attr_name, new_objects)

            else:
                setattr(instance, attr_name, value)

            await session.commit()
            return self._to_dict(instance)
