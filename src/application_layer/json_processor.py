from domain.exceptions import InputDataError
from domain.notification_sender_factory import NotificationSenderFactory
from infrastructure.processed_data_repository import ProcessedDataRepository
import ijson
from ijson.common import JSONError
from infrastructure.message_client import MessageClient
from domain.validators.email_notification_validator import EmailNotificationValidator
from domain.validators.exceptions import BadParametersError
from domain.validators.general_notification_validator import GeneralNotificationValidator
from domain.validators.post_notification_validator import PostNotificationValidator
from domain.validators.sms_notification_validator import SmsNotificationValidator


class JsonProcessor:

    def __init__(self, message_client: MessageClient,
                 processed_data_repository: ProcessedDataRepository) -> None:
        self.message_client = message_client
        self.processed_data_repository = processed_data_repository
        self.notification_sender_factory = NotificationSenderFactory(self.message_client)

    def process(self, json):
        try:
            for index, log_to_notify in enumerate(ijson.items(json, 'item')):
                self._send_notification(index, log_to_notify)
        except JSONError as e:
            raise InputDataError(e)
    
    def _send_notification(self, index: int, log_to_notify) -> None:
        if self.processed_data_repository.is_already_processed(index):
            return
        try:
            GeneralNotificationValidator().validate(log_to_notify)
            notification_sender = self.notification_sender_factory.get_sender(log_to_notify['type'])
            notification_sender.send(log_to_notify)
        except BadParametersError as e:
            self.processed_data_repository.append_invalid_item(index, log_to_notify)
        finally:
            self.processed_data_repository.append(index)
