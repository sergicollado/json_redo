import pytest
from unittest.mock import Mock
from message_client import MessageClient
from json_processor import json_processor

@pytest.fixture
def input_json():
    filename = 'tests/fixture_base.json'
    json_file = open(filename, "rb")
    yield json_file
    json_file.close()


def test_should_send_post_message(input_json):
    MessageClient.send_post = Mock()
    json_processor(input_json)
    MessageClient.send_post.assert_called()

def test_should_send_sms_message(input_json):
    MessageClient.send_sms = Mock()
    json_processor(input_json)
    MessageClient.send_sms.assert_called()

def test_should_send_email_message(input_json):
    MessageClient.send_email = Mock()
    json_processor(input_json)
    MessageClient.send_email.assert_called()