from abc import ABC, abstractmethod


class DatabaseTransaction(ABC):
    @abstractmethod
    async def start_transaction(self):
        raise NotImplementedError

    @abstractmethod
    async def commit_transaction(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback_transaction(self):
        raise NotImplementedError
