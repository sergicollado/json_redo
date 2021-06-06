from abc import abstractmethod
from abc import ABCMeta


class NotificationSenderAbstract(metaclass=ABCMeta):
    @abstractmethod
    def send(self, data) -> None:
        """send data to a client"""