from abc import ABC, abstractmethod
from sqlalchemy.future import select
from sqlalchemy.inspection import inspect
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

    def _to_dict(self, instance) -> Dict:
        """Конвертирует SQLAlchemy-объект в словарь (с поддержкой relationship)."""
        if hasattr(instance, "dict"):  # Если в SQLAlchemy 2.0 есть метод `.dict()`
            return instance.dict()

        serialized = {}
        mapper = inspect(instance)

        # Колонки (обычные поля модели)
        for column in mapper.mapper.column_attrs:
            serialized[column.key] = getattr(instance, column.key)

        # Отношения (relationship)
        for rel in mapper.mapper.relationships:
            related_obj = getattr(instance, rel.key)
            if related_obj is not None:
                if isinstance(related_obj, list):  # One-to-Many
                    serialized[rel.key] = [self._to_dict(obj) for obj in related_obj]
                else:  # One-to-One
                    serialized[rel.key] = self._to_dict(related_obj)

        return serialized

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
