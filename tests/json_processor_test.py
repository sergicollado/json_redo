import pytest
from unittest.mock import Mock
from message_client import MessageClient
from json_processor import json_processor

@pytest.fixture
def enter_json():
    return '''[
        {
        name: "John Doe 1",
        email: null,
        phone: null,
        url: http://example.com/push/,
        type: "post",
        }
    ]'''



def test_from_enter_json_must_call_proper_message_client_method(enter_json):
    filename = 'tests/fixture_base.json'
    message_client = Mock()
    with open(filename) as json_file:
        json_processor(json_file)
    message_client.send_post.assert_called()