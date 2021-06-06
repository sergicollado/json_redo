import pytest
from unittest.mock import Mock
from message_client import MessageClient
from json_processor import JsonProcessor
from validators.exceptions import BadParametersError
from processed_data_repository import ProcessedDataRepository
from validators import NotificationValidator

@pytest.fixture
def json_processor():
    repository = ProcessedDataRepository()
    yield JsonProcessor(MessageClient, repository)
    repository.data.clear()

@pytest.fixture
def input_json():
    filename = 'src/tests/fixture_post_error.json'
    json_file = open(filename, "rb")
    yield json_file
    json_file.close()


def test_should_raise_error_when_send_post_message_without_proper_params(input_json, json_processor):
    with pytest.raises(BadParametersError):
        json_processor.process(input_json)
