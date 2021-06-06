class BadParametersError(Exception):
    def __init__(self, validator_class, required_params: list, data: dict):
        self.validator_class = validator_class
        self.required_params = required_params
        self.data = data
        self.message = f'params: {" - ".join(required_params)} not found, data: {data}'
        super().__init__(self.message)

    def __str__(self):
        return self.message
