from domain.notification_sender_abstract import NotificationSenderAbstract
from domain.notification_types import NotificationType
from infrastructure.message_client import MessageClient
from domain.validators import PostNotificationValidator, SmsNotificationValidator, EmailNotificationValidator


class NotificationSenderFactory:
    def __init__(self, message_client: MessageClient):
        self.message_client = message_client
    
    def get_sender(self, sender_type: str):
        if sender_type == NotificationType.POST.value:
            return PostNotificationSender(self.message_client)
        if sender_type == NotificationType.SMS.value:
            return SmsNotificationSender(self.message_client)
        if sender_type == NotificationType.EMAIL.value:
            return EmailNotificationSender(self.message_client)


class PostNotificationSender(NotificationSenderAbstract):
    def __init__(self, message_client: MessageClient) -> None:
        self.message_client = message_client

    def send(self, data) -> None:
        PostNotificationValidator().validate(data)
        self.message_client.send_post(data['url'], data)

class SmsNotificationSender(NotificationSenderAbstract):
    def __init__(self, message_client: MessageClient) -> None:
        self.message_client = message_client

    def send(self, data) -> None:
        SmsNotificationValidator().validate(data)
        self.message_client.send_sms(data['phone'], data)

class EmailNotificationSender(NotificationSenderAbstract):
    def __init__(self, message_client: MessageClient) -> None:
        self.message_client = message_client

    def send(self, data) -> None:
        EmailNotificationValidator().validate(data)
        self.message_client.send_email(data['email'], data)