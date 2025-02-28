from abc import ABC, abstractmethod
from sqlalchemy.future import select
from sqlalchemy import inspect
from sqlalchemy.orm import class_mapper
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


class AbstractSQLRepository(AbstractRepository, ABC):
    def __init__(self, get_session, model):
        self.get_session = get_session
        self.model = model

    def _to_dict(self, instance, visited=None):
        if visited is None:
            visited = set()
            
        # Преобразуем колонки модели в словарь
        result = {
            column.key: getattr(instance, column.key)
            for column in class_mapper(instance.__class__).columns
        }
        
        # Получаем объект-инспектор для проверки состояния загрузки атрибутов
        state = inspect(instance)
        
        for name, relation in class_mapper(instance.__class__).relationships.items():
            if relation not in visited:
                visited.add(relation)
                
                # Если атрибут не загружен, он будет присутствовать в state.unloaded
                if name in state.unloaded:
                    # Возвращаем внешний ключ, если он определён
                    fk_value = getattr(instance, f"{name}_id", None)
                    if fk_value is not None:
                        result[f"{name}_id"] = fk_value
                else:
                    # Если атрибут загружен, обрабатываем его
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

    async def retrieve(self, pk: int) -> Optional[Dict]:
        async with self.get_session() as session:
            result = await session.execute(select(self.model).filter_by(id=pk))
            instance = result.scalar_one_or_none()
            return self._to_dict(instance) if instance else None

    async def retrieve_by_field(self, field_name: str, value: Any) -> Optional[Dict]:
        async with self.get_session() as session:
            query = select(self.model).filter(getattr(self.model, field_name) == value)
            result = await session.execute(query)
            instance = result.scalar_one_or_none()
            return self._to_dict(instance) if instance else None

    async def list(self) -> List[Dict]:
        async with self.get_session() as session:
            result = await session.execute(select(self.model))
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
