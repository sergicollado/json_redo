import pytest
from unittest.mock import Mock
from message_client import MessageClient
from json_processor import JsonProcessor
from processed_data_repository import ProcessedDataRepository

@pytest.fixture
def json_processor():
    repository = ProcessedDataRepository()
    yield JsonProcessor(MessageClient, repository)
    repository.data.clear()

@pytest.fixture
def input_json():
    filename = 'tests/fixture_base.json'
    json_file = open(filename, "rb")
    yield json_file
    json_file.close()


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
