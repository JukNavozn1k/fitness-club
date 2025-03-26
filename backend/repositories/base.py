from abc import ABC, abstractmethod
from sqlalchemy.future import select
from sqlalchemy import inspect, update, delete
from sqlalchemy.orm import class_mapper, Load, RelationshipProperty
from typing import List, Dict, Optional, Any
from collections import defaultdict
from beanie import Document,Link,BackLink
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
        


class AbstractMongoRepository(AbstractRepository):
    """
    Абстрактный репозиторий для MongoDB на базе Beanie с поддержкой Link-сущностей.
    Ожидается, что self.model является подклассом beanie.Document.
    """
    def __init__(self, model: Type[Document]):
        self.model = model

    # async def _prepare_data_with_links(self, data: Dict) -> Dict:
    #     """
    #     Обрабатывает данные перед созданием документа:
    #     Если поле модели является Link и в data передан словарь,
    #     то если словарь содержит идентификатор уже существующего объекта, то этот объект подставляется.
    #     Если идентификатора нет, выполняется поиск по фильтрам объекта и, если найден — используется.
    #     В противном случае создаётся новый документ.
    #     """
    #     for field, field_info in self.model.__fields__.items():
    #         if field in data and isinstance(data[field], dict):
    #             # Используем outer_type_ если доступен, иначе annotation
    #             field_type = getattr(field_info, "outer_type_", None) or field_info.annotation
    #             if hasattr(field_type, '__origin__') and field_type.__origin__ is Link:
    #                 linked_model = field_type.__args__[0]
    #                 link_data = data[field]
    #                 # Пытаемся извлечь идентификатор (id или _id)
    #                 link_id = link_data.get("id") or link_data.get("_id")
    #                 if link_id:
    #                     # Пробуем получить существующий документ по ID
    #                     existing_doc = await linked_model.get(link_id)
    #                     if existing_doc:
    #                         data[field] = existing_doc
    #                         continue
    #                 else:
    #                     # Если идентификатора нет, выполняем поиск по остальным полям
    #                     filters = {k: v for k, v in link_data.items() if k not in ("id", "_id")}
    #                     existing_docs = await linked_model.find(filters).to_list()
    #                     if existing_docs:
    #                         data[field] = existing_docs[0]
    #                         continue

    #                 # Если ничего не найдено – создаём новый документ
    #                 linked_instance = linked_model(**link_data)
    #                 await linked_instance.insert()
    #                 data[field] = linked_instance
    #     return data



    # async def _prepare_data_with_links(self, data: Dict) -> Dict:
    #     """
    #     Обрабатывает данные перед созданием документа:
    #     - Если поле модели является Link, то:
    #     - Если в данных присутствует id (или _id), пытается получить документ по нему.
    #     - Иначе выполняет поиск по остальным полям.
    #     - Если документ не найден, создаётся новый.
    #     - Если поле модели является List[Link], то:
    #     - Сначала для тех элементов, где передан id, агрегированно запрашиваются все документы.
    #     - Для остальных элементов собираются фильтры и выполняется единый запрос с $or по всем фильтрам.
    #     - Затем для каждого элемента списка:
    #         * Если найден документ по id – используется он.
    #         * Если по фильтру – выбирается первый подходящий.
    #         * Если ничего не найдено – создаётся новый документ.
    #     """
    #     for field, field_info in self.model.__fields__.items():
    #         if field in data:
    #             # Используем outer_type_ если доступен, иначе annotation
    #             field_type = getattr(field_info, "outer_type_", None) or field_info.annotation

    #             if hasattr(field_type, '__origin__'):
    #                 origin_type = field_type.__origin__

    #                 # Обработка одиночного Link
    #                 if origin_type is Link:
    #                     linked_model = field_type.__args__[0]
    #                     link_data = data[field]
    #                     link_id = link_data.get("id") or link_data.get("_id")
    #                     if link_id:
    #                         existing_doc = await linked_model.get(link_id)
    #                         if existing_doc:
    #                             data[field] = existing_doc
    #                             continue
    #                     else:
    #                         filters = {k: v for k, v in link_data.items() if k not in ("id", "_id")}
    #                         existing_docs = await linked_model.find(filters).to_list()
    #                         if existing_docs:
    #                             data[field] = existing_docs[0]
    #                             continue

    #                     # Если ничего не найдено – создаём новый документ
    #                     linked_instance = linked_model(**link_data)
    #                     await linked_instance.insert()
    #                     data[field] = linked_instance

    #                 # Обработка списка List[Link]
    #                 elif origin_type in (list, List) and hasattr(field_type.__args__[0], '__origin__') and field_type.__args__[0].__origin__ is Link:
    #                     linked_model = field_type.__args__[0].__args__[0]
    #                     link_data_list = data[field]

    #                     # 1. Обработка элементов, где передан id
    #                     link_ids = [link_data.get("id") or link_data.get("_id")
    #                                 for link_data in link_data_list
    #                                 if link_data.get("id") or link_data.get("_id")]
    #                     existing_docs_dict = {}
    #                     if link_ids:
    #                         existing_docs = await linked_model.find({"_id": {"$in": link_ids}}).to_list()
    #                         existing_docs_dict = {str(doc["_id"]): doc for doc in existing_docs}

    #                     # 2. Для элементов без id собираем фильтры (каждый фильтр – словарь остальных полей)
    #                     # При этом собираем список фильтров для агрегированного запроса.
    #                     no_id_indexes = []
    #                     filters_list = []
    #                     for idx, link_data in enumerate(link_data_list):
    #                         if not (link_data.get("id") or link_data.get("_id")):
    #                             no_id_indexes.append(idx)
    #                             filters = {k: v for k, v in link_data.items() if k not in ("id", "_id")}
    #                             filters_list.append(filters)

    #                     # Выполняем один агрегированный запрос для всех фильтров (если они есть)
    #                     aggregated_docs = []
    #                     if filters_list:
    #                         # Формируем список условий: для каждого фильтр-словаря условие $and: [<filter dict>]
    #                         # (условие $and с одним элементом можно использовать для унификации формата)
    #                         or_query = {"$or": [{"$and": [flt]} for flt in filters_list]}
    #                         aggregated_docs = await linked_model.find(or_query).to_list()

    #                     # 3. Для каждого элемента списка подбираем соответствующий документ
    #                     updated_list = []
    #                     for idx, link_data in enumerate(link_data_list):
    #                         link_id = link_data.get("id") or link_data.get("_id")
    #                         if link_id and str(link_id) in existing_docs_dict:
    #                             # Если по id найден документ
    #                             updated_list.append(existing_docs_dict[str(link_id)])
    #                         else:
    #                             # Формируем фильтр для текущего элемента
    #                             filters = {k: v for k, v in link_data.items() if k not in ("id", "_id")}
    #                             # Ищем первый документ из агрегированного результата, удовлетворяющий фильтру
    #                             matched = None
    #                             for doc in aggregated_docs:
    #                                 if all(doc.get(k) == v for k, v in filters.items()):
    #                                     matched = doc
    #                                     break
    #                             if matched:
    #                                 updated_list.append(matched)
    #                             else:
    #                                 # Если ничего не найдено – создаём новый документ
    #                                 linked_instance = linked_model(**link_data)
    #                                 await linked_instance.insert()
    #                                 updated_list.append(linked_instance)
    #                     data[field] = updated_list
    #     return data

    # async def _prepare_data_with_links(self, data: Dict) -> Dict:
    #     """
    #     Обрабатывает данные перед созданием документа с batch-операциями.
    #     """
        
    #     # Регистр для массовых операций
    #     link_operations = defaultdict(lambda: {
    #         'ids': set(),
    #         'filters': [],
    #         'new_docs': [],
    #         'model': None
    #     })

    #     # Первый проход: сбор всех ссылок
    #     for field, field_info in self.model.__fields__.items():
    #         if field not in data:
    #             continue

    #         field_type = getattr(field_info, "outer_type_", None) or field_info.annotation
    #         if not hasattr(field_type, '__origin__'):
    #             continue

    #         origin_type = field_type.__origin__

    #         # Обработка одиночного Link
    #         if origin_type is Link:
    #             linked_model = field_type.__args__[0]
    #             link_data = data[field]
    #             link_id = link_data.get("id") or link_data.get("_id")
                
    #             key = f"single_{linked_model.__name__}"
    #             link_operations[key]['model'] = linked_model
                
    #             if link_id:
    #                 link_operations[key]['ids'].add(link_id)
    #             else:
    #                 link_operations[key]['filters'].append(
    #                     {k: v for k, v in link_data.items() if k not in ("id", "_id")}
    #                 )

    #         # Обработка List[Link]
    #         elif origin_type in (list, List) and hasattr(field_type.__args__[0], '__origin__') and field_type.__args__[0].__origin__ is Link:
    #             linked_model = field_type.__args__[0].__args__[0]
    #             link_data_list = data[field]
                
    #             key = f"list_{linked_model.__name__}"
    #             link_operations[key]['model'] = linked_model
                
    #             for link_data in link_data_list:
    #                 link_id = link_data.get("id") or link_data.get("_id")
    #                 if link_id:
    #                     link_operations[key]['ids'].add(link_id)
    #                 else:
    #                     link_operations[key]['filters'].append(
    #                         {k: v for k, v in link_data.items() if k not in ("id", "_id")}
    #                     )
    #                 link_operations[key]['new_docs'].append(link_data)

    #     # Массовый поиск документов
    #     found_docs = defaultdict(dict)
    #     for key, op in link_operations.items():
    #         model = op['model']
    #         query = {"$or": []}
            
    #         if op['ids']:
    #             query["$or"].append({"_id": {"$in": list(op['ids'])}})
            
    #         if op['filters']:
    #             query["$or"].extend([{"$and": [flt]} for flt in op['filters']])
            
    #         if query["$or"]:
    #             docs = await model.find(query).to_list()
    #             found_docs[key] = {
    #                 str(doc.id): doc for doc in docs
    #             }

    #     # Массовая вставка новых документов
    #     new_docs_cache = defaultdict(dict)
    #     for key, op in link_operations.items():
    #         model = op['model']
    #         new_docs = []
            
    #         for doc_data in op['new_docs']:
    #             doc_id = doc_data.get("id") or doc_data.get("_id")
    #             if not doc_id and not any(
    #                 doc_data.items() <= doc.items()
    #                 for doc in found_docs[key].values()
    #             ):
    #                 new_docs.append(model(**doc_data))
            
    #         if new_docs:
    #             inserted = await model.insert_many(new_docs)
    #             new_docs_cache[key] = {str(doc.id): doc for doc in inserted}

    #     # Второй проход: замена данных
    #     for field, field_info in self.model.__fields__.items():
    #         if field not in data:
    #             continue

    #         field_type = getattr(field_info, "outer_type_", None) or field_info.annotation
    #         if not hasattr(field_type, '__origin__'):
    #             continue

    #         origin_type = field_type.__origin__

    #         if origin_type is Link:
    #             linked_model = field_type.__args__[0]
    #             link_data = data[field]
    #             key = f"single_{linked_model.__name__}"
                
    #             doc_id = str(link_data.get("id") or link_data.get("_id"))
    #             data[field] = found_docs[key].get(doc_id) or new_docs_cache[key].get(doc_id)

    #         elif origin_type in (list, List) and hasattr(field_type.__args__[0], '__origin__') and field_type.__args__[0].__origin__ is Link:
    #             linked_model = field_type.__args__[0].__args__[0]
    #             link_data_list = data[field]
    #             key = f"list_{linked_model.__name__}"
                
    #             updated_list = []
    #             for link_data in link_data_list:
    #                 doc_id = str(link_data.get("id") or link_data.get("_id"))
    #                 filters = {k: v for k, v in link_data.items() if k not in ("id", "_id")}
                    
    #                 # Ищем сначала по ID, потом по фильтрам
    #                 if doc_id:
    #                     doc = found_docs[key].get(doc_id) or new_docs_cache[key].get(doc_id)
    #                 else:
    #                     doc = next(
    #                         (d for d in found_docs[key].values() 
    #                         if filters.items() <= d.dict().items()),
    #                         None
    #                     )
                    
    #                 if not doc:
    #                     doc = new_docs_cache[key].get(
    #                         next(k for k, v in new_docs_cache[key].items() 
    #                             if filters.items() <= v.dict().items())
    #                     )
                    
    #                 updated_list.append(doc or linked_model(**link_data))
                
    #             data[field] = updated_list

    #     return data


    async def _prepare_data_with_links(self, data: Dict) -> Dict:
        """
        Обрабатывает данные перед созданием документа с batch-операциями.
        """
        
        # Регистр для массовых операций
        link_operations = defaultdict(lambda: {
            'ids': set(),
            'filters': [],
            'new_docs': [],
            'model': None
        })

        # Первый проход: сбор всех ссылок
        for field, field_info in self.model.__fields__.items():
            if field not in data:
                continue

            field_type = getattr(field_info, "outer_type_", None) or field_info.annotation
            if not hasattr(field_type, '__origin__'):
                continue

            origin_type = field_type.__origin__

            # Обработка одиночных Link и BackLink
            if origin_type in (Link, BackLink):
                linked_model = field_type.__args__[0]
                link_data = data[field]
                link_id = link_data.get("id") or link_data.get("_id")
                
                key = f"single_{origin_type.__name__}_{linked_model.__name__}"
                link_operations[key]['model'] = linked_model
                
                if link_id:
                    link_operations[key]['ids'].add(link_id)
                else:
                    link_operations[key]['filters'].append(
                        {k: v for k, v in link_data.items() if k not in ("id", "_id")}
                    )

            # Обработка List[Link] и List[BackLink]
            elif origin_type in (list, List) and len(field_type.__args__) > 0:
                item_type = field_type.__args__[0]
                if hasattr(item_type, '__origin__') and item_type.__origin__ in (Link, BackLink):
                    link_origin = item_type.__origin__
                    linked_model = item_type.__args__[0]
                    link_data_list = data[field]
                    
                    key = f"list_{link_origin.__name__}_{linked_model.__name__}"
                    link_operations[key]['model'] = linked_model
                    
                    for link_data in link_data_list:
                        link_id = link_data.get("id") or link_data.get("_id")
                        if link_id:
                            link_operations[key]['ids'].add(link_id)
                        else:
                            link_operations[key]['filters'].append(
                                {k: v for k, v in link_data.items() if k not in ("id", "_id")}
                            )
                        link_operations[key]['new_docs'].append(link_data)

        # Массовый поиск документов
        found_docs = defaultdict(dict)
        for key, op in link_operations.items():
            model = op['model']
            query = {"$or": []}
            
            if op['ids']:
                query["$or"].append({"_id": {"$in": list(op['ids'])}})
            
            if op['filters']:
                query["$or"].extend([{"$and": [flt]} for flt in op['filters']])
            
            if query["$or"]:
                docs = await model.find(query).to_list()
                found_docs[key] = {
                    str(doc.id): doc for doc in docs
                }

        # Массовая вставка новых документов
        new_docs_cache = defaultdict(dict)
        for key, op in link_operations.items():
            model = op['model']
            new_docs = []
            
            for doc_data in op['new_docs']:
                doc_id = doc_data.get("id") or doc_data.get("_id")
                if not doc_id and not any(
                    doc_data.items() <= doc.items()
                    for doc in found_docs[key].values()
                ):
                    new_docs.append(model(**doc_data))
            
            if new_docs:
                inserted = await model.insert_many(new_docs)
                new_docs_cache[key] = {str(doc.id): doc for doc in inserted}

        # Второй проход: замена данных
        for field, field_info in self.model.__fields__.items():
            if field not in data:
                continue

            field_type = getattr(field_info, "outer_type_", None) or field_info.annotation
            if not hasattr(field_type, '__origin__'):
                continue

            origin_type = field_type.__origin__

            # Обработка Link/BackLink
            if origin_type in (Link, BackLink):
                linked_model = field_type.__args__[0]
                link_data = data[field]
                key = f"single_{origin_type.__name__}_{linked_model.__name__}"
                
                doc_id = str(link_data.get("id") or link_data.get("_id"))
                data[field] = found_docs[key].get(doc_id) or new_docs_cache[key].get(doc_id)

            # Обработка List[Link]/List[BackLink]
            elif origin_type in (list, List) and len(field_type.__args__) > 0:
                item_type = field_type.__args__[0]
                if hasattr(item_type, '__origin__') and item_type.__origin__ in (Link, BackLink):
                    link_origin = item_type.__origin__
                    linked_model = item_type.__args__[0]
                    link_data_list = data[field]
                    key = f"list_{link_origin.__name__}_{linked_model.__name__}"
                    
                    updated_list = []
                    for link_data in link_data_list:
                        doc_id = str(link_data.get("id") or link_data.get("_id"))
                        filters = {k: v for k, v in link_data.items() if k not in ("id", "_id")}
                        
                        # Ищем сначала по ID, потом по фильтрам
                        if doc_id:
                            doc = found_docs[key].get(doc_id) or new_docs_cache[key].get(doc_id)
                        else:
                            doc = next(
                                (d for d in found_docs[key].values() 
                                if filters.items() <= d.dict().items()),
                                None
                            )
                        
                        if not doc:
                            doc = new_docs_cache[key].get(
                                next((k for k, v in new_docs_cache[key].items() 
                                    if filters.items() <= v.dict().items()), None)
                            )
                        
                        updated_list.append(doc or linked_model(**link_data))
                    
                    data[field] = updated_list

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
        Рекурсивно заполняет поле по указанному пути (например, "profile.test").
        На каждом уровне, если поле является ссылкой (Link), вызывается fetch_link.
        """
        parts = field_path.split('.')
        current_document = document
        for part in parts:
            if hasattr(current_document, 'fetch_link'):
                # Передаём имя поля, чтобы загрузить связанный документ
                await current_document.fetch_link(part)
            current_document = getattr(current_document, part, None)
            if current_document is None:
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