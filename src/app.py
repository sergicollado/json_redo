import urllib.request
from application_layer.json_processor import JsonProcessor
from infraestructure.message_client import MessageClient
from infraestructure.processed_data_repository import ProcessedDataRepository


def main():
    url = 'https://raw.githubusercontent.com/UN-ICC/notifications-processor/master/notifications_log.json'
    
    repository = ProcessedDataRepository()

    try:
        with urllib.request.urlopen(url) as f:
            JsonProcessor(MessageClient, repository).process(f)
    except Exception as e:
        print(f'Something wrong happened: {e}')

if __name__ == '__main__':
    main()