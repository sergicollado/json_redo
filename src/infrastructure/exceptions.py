class PersistenceFileError(Exception):
    def __init__(self, filename, exception_raised:Exception):
        self.message = f'Error Reading or Writing file: {filename} {exception_raised}'
        super().__init__(self.message)

    def __str__(self):
        return self.message
