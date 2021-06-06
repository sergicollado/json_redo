import urllib.request
from application_layer.json_processor import JsonProcessor
from infraestructure.message_client import MessageClient
from infraestructure.processed_data_repository import ProcessedDataRepository


def main():
    url = 'https://raw.githubusercontent.com/UN-ICC/notifications-processor/master/notifications_log.json'
    
    repository = ProcessedDataRepository()

    with urllib.request.urlopen(url) as f:
        JsonProcessor(MessageClient, repository).process(f)


if __name__ == '__main__':
    main()