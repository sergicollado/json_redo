from domain.validators.exceptions import BadParametersError
from domain.validators.abstract_classes import NotificationValidator 


class PostNotificationValidator(NotificationValidator):    
    @property                 
    def required_params(self):     
        return ["url", "name"]