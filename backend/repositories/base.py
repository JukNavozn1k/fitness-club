from abc import ABC, abstractmethod

from sqlalchemy.future import select
from typing import List, Dict, Type, TypeVar, Optional

T = TypeVar('T') 

class AbstractRepository(ABC):
    @abstractmethod
    async def create(self, data: Dict) -> T:
        """
        Создает новый объект и возвращает его.
        """
        raise NotImplementedError

    @abstractmethod
    async def retrieve(self, pk: int) -> Optional[T]:
        """
        Извлекает объект по его первичному ключу.
        Возвращает объект модели или None, если объект не найден.
        """
        raise NotImplementedError

    @abstractmethod
    async def list(self) -> List[T]:
        """
        Извлекает список всех объектов.
        Возвращает список объектов модели.
        """
        raise NotImplementedError

    @abstractmethod
    async def update(self, pk: int, data: Dict) -> Optional[T]:
        """
        Обновляет объект с указанным первичным ключом.
        Возвращает обновленный объект или None, если объект не найден.
        """
        raise NotImplementedError

    @abstractmethod
    async def delete(self, pk: int) -> bool:
        """
        Удаляет объект с указанным первичным ключом.
        Возвращает True, если объект был удален, иначе False.
        """
        raise NotImplementedError



class AbstractSQLRepository(AbstractRepository, ABC):
    def __init__(self, get_session, model: Type[T]):
        self.get_session = get_session  # Передаем функцию get_session
        self.model = model  # Модель передается в конструкторе

    async def create(self, data: dict) -> T:
        async with self.get_session() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            return instance

    async def retrieve(self, pk: int) -> Optional[T]:
        async with self.get_session() as session:
            result = await session.execute(select(self.model).filter(self.model.id == pk))
            return result.scalar_one_or_none()

    async def list(self) -> List[T]:
        async with self.get_session() as session:
            result = await session.execute(select(self.model))
            return result.scalars().all()

    async def update(self, pk: int, data: dict) -> Optional[T]:
        async with self.get_session() as session:
            result = await session.execute(select(self.model).filter(self.model.id == pk))
            instance = result.scalar_one_or_none()
            if instance:
                for key, value in data.items():
                    setattr(instance, key, value)
                await session.commit()
                return instance
            return None

    async def delete(self, pk: int) -> bool:
        async with self.get_session() as session:
            result = await session.execute(select(self.model).filter(self.model.id == pk))
            instance = result.scalar_one_or_none()
            if instance:
                await session.delete(instance)
                await session.commit()
                return True
            return False