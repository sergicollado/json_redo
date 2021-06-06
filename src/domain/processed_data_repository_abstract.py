from abc import abstractmethod
from abc import ABCMeta


class ProcessedDataRepositoryAbstract(metaclass=ABCMeta):

    @abstractmethod
    def append(self, index: int) -> None:
        pass
    @abstractmethod
    def is_already_processed(self, index: int) ->bool:
        pass
    @abstractmethod
    def append_invalid_item(self, index: int, data: dict)-> None:
        pass
    @abstractmethod
    def get_invalid_item(self, index: int) -> dict:
        pass