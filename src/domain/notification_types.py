from enum import Enum, auto

class NotificationType(Enum):
    POST = 'post'
    SMS = 'sms'
    EMAIL = 'email'