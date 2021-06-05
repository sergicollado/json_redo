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


def test_from_enter_json_must_call_proper_message_client_method(input_json):
    
    MessageClient.send_post = Mock()
    json_processor(input_json)
    MessageClient.send_post.assert_called()