from validators.exceptions import BadParametersError
from validators.abstract_classes import NotificationValidator 


class GeneralNotificationValidator(NotificationValidator):    
    @property                 
    def required_params(self):     
        return ["type", "name"]