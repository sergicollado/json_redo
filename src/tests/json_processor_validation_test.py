import pytest
from unittest.mock import MagicMock, Mock
from message_client import MessageClient
from json_processor import JsonProcessor
from validators.exceptions import BadParametersError
from processed_data_repository import ProcessedDataRepository
from validators import NotificationValidator


@pytest.fixture
def processed_repository():
    repository = ProcessedDataRepository()
    yield repository
    repository.data.clear()

@pytest.fixture
def json_processor(processed_repository):
    return JsonProcessor(MessageClient, processed_repository)


@pytest.fixture
def input_json():
    filename = 'src/tests/fixture_post_error.json'
    json_file = open(filename, "rb")
    yield json_file
    json_file.close()


def test_should_save_invalid_items(input_json, json_processor, processed_repository):
    json_processor.process(input_json)
    expected_invalid_item_indices = [0,2]
    for index in expected_invalid_item_indices:
        assert processed_repository.get_invalid_item(index)
