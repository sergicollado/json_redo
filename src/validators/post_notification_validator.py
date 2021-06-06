from validators.exceptions import BadParametersError
from validators.abstract_classes import NotificationValidator 


class PostNotificationValidator(NotificationValidator):    
    @property                 
    def required_params(self):     
        return ["url", "name"]