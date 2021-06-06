from abc import abstractmethod, abstractstaticmethod
from abc import ABCMeta

from validators.exceptions import BadParametersError

class NotificationValidator(metaclass=ABCMeta):
    @property
    @abstractmethod
    def required_params(self) -> list:
        pass
    
    def validate(self, data: dict) -> None:
        errors = []
        print('REQUIRED PARAMS')
        print(self.required_params)
        for required in self.required_params:
            if not required in data or not data[required]:
                errors.append(required)
        if errors:
            raise BadParametersError({self.__class__}, errors)