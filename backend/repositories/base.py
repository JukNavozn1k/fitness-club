from abc import ABC,abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def create(data):
        raise NotImplementedError
    @abstractmethod
    async def retrieve(pk : int):
        raise NotImplementedError

    @abstractmethod
    async def list():
        raise NotImplementedError

    @abstractmethod
    async def update(pk : int,data : dict):
        raise NotImplementedError
    @abstractmethod
    async def delete(pk : int):
        raise NotImplementedError

class AbstractSQLRepository(AbstractRepository):
    model = None

    # ToDo определить базовые методы 
    # @abstractmethod
    # async def create(data):
    #     raise NotImplementedError
    # @abstractmethod
    # async def retrieve(pk : int):
    #     raise NotImplementedError

    # @abstractmethod
    # async def list():
    #     raise NotImplementedError

    # @abstractmethod
    # async def update(pk : int,data : dict):
    #     raise NotImplementedError
    # @abstractmethod
    # async def delete(pk : int):
    #     raise NotImplementedError
