import urllib.request
import pprint
from application_layer.json_processor import JsonProcessor
from infrastructure.message_client import MessageClient
from infrastructure.processed_data_repository_persistence import ProcessedDataRepositoryPersistence


def main():
    url = 'https://raw.githubusercontent.com/UN-ICC/notifications-processor/master/notifications_log.json'
    
    persistence_filename = 'processed_data.json'
    repository = ProcessedDataRepositoryPersistence(persistence_filename)

    try:
        with urllib.request.urlopen(url) as f:
            JsonProcessor(MessageClient, repository).process(f)
            repository.save()
            print('Invalid Items: ')
            pprint.pprint(repository.get_invalid_items())

    except Exception as e:
        print(f'Something wrong happened: {e}')

if __name__ == '__main__':
    main()