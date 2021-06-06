from decimal import Underflow
from domain.validators.exceptions import BadParametersError
import pytest

from domain.validators.general_notification_validator import GeneralNotificationValidator

@pytest.fixture
def json_data():
    return     {
    "name": "John Doe 1",
    "email": None,
    "phone": None,
    "url": "http: //example.com/push/",
    "type": "post"
    }

def test_should_format_message_properly(json_data):
    validator_class = GeneralNotificationValidator
    required_params = ['param_a', 'param_b']
    expected_message = f'{validator_class.__name__} params: {" - ".join(required_params)} not found, data: {json_data}'
    try:
        raise BadParametersError(validator_class.__name__, required_params, json_data)
    except BadParametersError as e:
        assert e.message == expected_message