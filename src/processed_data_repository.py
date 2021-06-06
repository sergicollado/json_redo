


class ProcessedDataRepository:
    data = []
    invalid_items = []

    def append(self, index: int) -> None:
        self.data.append(index)

    def is_already_processed(self, index: int) ->bool:
        return index in self.data
    
    def append_invalid_item(self, index: int, data: dict)-> None:
        data_with_index = {
            "index": index,
            "data": data
        }
        self.invalid_items.append(data_with_index)

    def get_invalid_item(self, index: int) -> dict:
        print(self.invalid_items)
        item =  [item for item in self.invalid_items if item['index'] == index]
        return item[0]