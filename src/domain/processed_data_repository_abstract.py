from abc import abstractmethod
from abc import ABCMeta


class ProcessedDataRepositoryAbstract(metaclass=ABCMeta):

    @abstractmethod
    def append(self, index: int) -> None:
        """insert already processed data"""
    @abstractmethod
    def is_already_processed(self, index: int) ->bool:
        """check if is already processed index item"""
    @abstractmethod
    def append_invalid_item(self, index: int, data: dict)-> None:
        """insert invalid already processed data"""
    @abstractmethod
    def get_invalid_item(self, index: int) -> dict:
        """get and invalid item"""