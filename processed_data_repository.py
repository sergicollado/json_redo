class ProcessedDataRepository:
    data = []

    def append(self, index: int) -> None:
        self.data.append(index)

    def is_already_processed(self, index: int) ->bool:
        return index in self.data