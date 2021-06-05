from processed_data_repository import ProcessedDataRepository
import ijson
from message_client import MessageClient

class JsonProcessor:
    def __init__(self, message_client: MessageClient, processed_data_repository: ProcessedDataRepository) -> None:
        self.message_client = message_client
        self.processed_data_repository = processed_data_repository

    def process(self, json):
        for index, entry_log in enumerate(ijson.items(json, 'item')):
            self.process_log(index, entry_log)

    def process_log(self, index: int, entry_log) -> None:
        if self.processed_data_repository.is_already_processed(index):
            print(f'ALREADY PROCESSED {index}')
            return
        print(f'TO PROCESS {index}')
        self.process_post(entry_log)
        self.process_sms(entry_log)
        self.process_email(entry_log)
        self.processed_data_repository.append(index)

    def process_post(self, data: dict) -> None:
        if data['type'] != 'post':
            return
        self.message_client.send_post(data['url'], data)

    def process_sms(self, data: dict) -> None:
        if data['type'] != 'sms':
            return
        self.message_client.send_sms(data['phone'], data)

    def process_email(self, data: dict) -> None:
        if data['type'] != 'email':
            return
        self.message_client.send_email(data['email'], data)