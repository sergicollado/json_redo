


import json
from json.decoder import JSONDecodeError
from domain.processed_data_repository_abstract import ProcessedDataRepositoryAbstract
from infrastructure.exceptions import PersistenceFileError



class ProcessedDataRepositoryPersistence(ProcessedDataRepositoryAbstract):
    
    def __init__(self, file: str) -> None:
        super().__init__()
        self.file = file
        self._load_file_data()

    def _load_file_data(self):
        try:
            with open(self.file, 'r') as data_file:
                data = json.load(data_file)
                self.data = data.get('processed_data', [])
                self.invalid_items = data.get('invalid_items', []) 
        except JSONDecodeError as e:
            self._default_init()
        except FileNotFoundError as e:
            self._default_init()
        except Exception as e:
            raise PersistenceFileError(self.file, e)

    def _default_init(self):
        self.data = []
        self.invalid_items = []

    def append(self, index: int) -> None:
        self.data.append(index)

    def is_already_processed(self, index: int) ->bool:
        return index < len(self.data)
    
    def append_invalid_item(self, index: int, data: dict)-> None:
        data_with_index = {
            "index": index,
            "data": data
        }
        self.invalid_items.append(data_with_index)

    def get_invalid_item(self, index: int) -> dict:
        item =  [item for item in self.invalid_items if item['index'] == index]
        return item[0]
    
    def save(self):
        with open(self.file, 'w') as outfile:
            data = {
                'processed_data' : self.data,
                'invalid_items' : self.invalid_items
            }
            try:
                json.dump(data, outfile)
            except Exception as e:
                print(e)

    def get_invalid_items(self):
        return self.invalid_items