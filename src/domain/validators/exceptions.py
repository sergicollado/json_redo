
class BadParametersError(Exception):
    def __init__(self, class_name: str, required_params: list, data: dict):
        self.message = f'{class_name} params: {" - ".join(required_params)} not found, data: {data}'
        super().__init__(self.message)

    def __str__(self):
        return self.message
