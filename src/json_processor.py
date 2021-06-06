from processed_data_repository import ProcessedDataRepository
import ijson
from message_client import MessageClient
from validators.exceptions import BadParametersError
from validators.post_notification_validator import PostNotificationValidator


class JsonProcessor:
    def __init__(self, message_client: MessageClient,
                 processed_data_repository: ProcessedDataRepository) -> None:
        self.message_client = message_client
        self.processed_data_repository = processed_data_repository

    def process(self, json):
        for index, log_to_notify in enumerate(ijson.items(json, 'item')):
            self.send_notification(index, log_to_notify)

    def send_notification(self, index: int, log_to_notify) -> None:
        if self.processed_data_repository.is_already_processed(index):
            return
        try:
            self.process_post(log_to_notify)
            self.process_sms(log_to_notify)
            self.process_email(log_to_notify)
        except BadParametersError as e:
            self.processed_data_repository.append_invalid_item(index, log_to_notify)
        finally:
            self.processed_data_repository.append(index)

    def process_post(self, data: dict) -> None:
        if data['type'] != 'post':
            return
        PostNotificationValidator().validate(data)
        self.message_client.send_post(data['url'], data)

    def process_sms(self, data: dict) -> None:
        if data['type'] != 'sms':
            return
        self.message_client.send_sms(data['phone'], data)

    def process_email(self, data: dict) -> None:
        if data['type'] != 'email':
            return
        self.message_client.send_email(data['email'], data)