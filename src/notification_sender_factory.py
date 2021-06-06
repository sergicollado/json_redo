from message_client import MessageClient
from validators import PostNotificationValidator, SmsNotificationValidator, EmailNotificationValidator


class NotificationSenderFactory:
    def __init__(self, message_client: MessageClient):
        self.message_client = message_client
    
    def get_sender(self, sender_type: str):
        if sender_type == 'post':
            return PostNotificationSender(self.message_client)
        if sender_type == 'sms':
            return SmsNotificationSender(self.message_client)
        if sender_type == 'email':
            return EmailNotificationSender(self.message_client)


class PostNotificationSender:
    def __init__(self, message_client: MessageClient) -> None:
        self.message_client = message_client

    def send(self, data):
        PostNotificationValidator().validate(data)
        self.message_client.send_post(data['url'], data)

class SmsNotificationSender:
    def __init__(self, message_client: MessageClient) -> None:
        self.message_client = message_client

    def send(self, data):
        SmsNotificationValidator().validate(data)
        self.message_client.send_sms(data['phone'], data)

class EmailNotificationSender:
    def __init__(self, message_client: MessageClient) -> None:
        self.message_client = message_client

    def send(self, data):
        EmailNotificationValidator().validate(data)
        self.message_client.send_email(data['email'], data)