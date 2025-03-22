from abc import ABC, abstractmethod
from sqlalchemy.future import select
from sqlalchemy import inspect, update, delete
from sqlalchemy.orm import class_mapper, Load, RelationshipProperty
from typing import List, Dict, Optional, Any

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
    async def retrieve_by_field(self, field_name: str, value: Any, filters: Optional[Dict[str, Any]] = None) -> Optional[Dict]:
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