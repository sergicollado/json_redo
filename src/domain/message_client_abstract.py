from abc import abstractstaticmethod
from abc import ABCMeta


class MessageClientAbstract(metaclass=ABCMeta):
    @abstractstaticmethod
    def send_post(url: str, data: dict) -> None:
        pass
    @abstractstaticmethod
    def send_sms(phone: str, data: dict) -> None:
        pass
    @abstractstaticmethod
    def send_email(email: str, data: dict) -> None:
        pass