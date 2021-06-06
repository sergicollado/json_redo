import pytest
from unittest.mock import Mock
from domain.exceptions import InputDataError
from infraestructure.message_client import MessageClient
from application_layer.json_processor import JsonProcessor
from infraestructure.processed_data_repository import ProcessedDataRepository

@pytest.fixture
def json_processor():
    repository = ProcessedDataRepository()
    yield JsonProcessor(MessageClient, repository)
    repository.data.clear()

@pytest.fixture
def input_json():
    filename = 'src/tests/fixture_base.json'
    json_file = open(filename, "rb")
    yield json_file
    json_file.close()


@pytest.fixture
def error_input_json():
    filename = 'src/tests/fixture_bad_format.json'
    json_file = open(filename, "rb")
    yield json_file

def test_should_send_post_message_with_proper_params(input_json, json_processor):
    MessageClient.send_post = Mock()
    json_processor.process(input_json)
    expected_url = 'http: //example.com/push/'
    expected_data = {
        "name": "John Doe 1",
        "email": None,
        "phone": None,
        "url": "http: //example.com/push/",
        "type": "post"
    }
    MessageClient.send_post.assert_called_once_with(expected_url,
                                                    expected_data)


def test_should_send_sms_message_with_proper_params(input_json, json_processor):
    MessageClient.send_sms = Mock()
    json_processor.process(input_json)

    expected_phone = '+34692018264'
    expected_data = {
        "name": "John Doe 3",
        "email": None,
        "phone": "+34692018264",
        "url": None,
        "type": "sms"
    }
    MessageClient.send_sms.assert_called_once_with(expected_phone, expected_data)


def test_should_send_email_message_with_proper_params(input_json, json_processor):
    MessageClient.send_email = Mock()
    json_processor.process(input_json)

    expected_email = 'doe@example.com'
    expected_data = {
    "name": "John Doe 2",
    "email": "doe@example.com",
    "phone": None,
    "url": "http: //example.com",
    "type": "email"
    }
    MessageClient.send_email.assert_called_once_with(expected_email, expected_data)

def test_should_raise_input_data_error_if_json_has_not_a_proper_format(error_input_json, json_processor):
    with pytest.raises(InputDataError):
        json_processor.process(error_input_json)