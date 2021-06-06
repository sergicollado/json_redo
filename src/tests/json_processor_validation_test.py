import pytest
from unittest.mock import MagicMock, Mock
from message_client import MessageClient
from json_processor import JsonProcessor
from validators.exceptions import BadParametersError
from processed_data_repository import ProcessedDataRepository



@pytest.fixture
def processed_repository():
    repository = ProcessedDataRepository()
    yield repository
    repository.data.clear()
    repository.invalid_items.clear()

@pytest.fixture
def json_processor(processed_repository):
    return JsonProcessor(MessageClient, processed_repository)


@pytest.fixture
def post_errors_input_json():
    filename = 'src/tests/fixture_post_error.json'
    json_file = open(filename, "rb")
    yield json_file
    json_file.close()

@pytest.fixture
def error_input_json():
    filename = 'src/tests/fixture_with_error.json'
    json_file = open(filename, "rb")
    yield json_file
    json_file.close()


@pytest.fixture
def no_type_input_json():
    filename = 'src/tests/fixture_with_no_type_error.json'
    json_file = open(filename, "rb")
    yield json_file
    json_file.close()

def test_should_save_invalid_type_post_items(post_errors_input_json, json_processor, processed_repository):
    json_processor.process(post_errors_input_json)
    expected_invalid_item_indices = [0,2]
    for index in expected_invalid_item_indices:
        assert processed_repository.get_invalid_item(index)

def test_should_save_every_type_notification_with_invalid_params(error_input_json, json_processor, processed_repository):
    json_processor.process(error_input_json)
    expected_invalid_item_indices = [0,1,2,3,4,5]
    for index in expected_invalid_item_indices:
        assert processed_repository.get_invalid_item(index)

def test_should_save_general_notification_error_when_item_has_not_type_or_name(no_type_input_json, json_processor, processed_repository):
    json_processor.process(no_type_input_json)
    expected_invalid_item_indices = [0,2,4]
    for index in expected_invalid_item_indices:
        assert processed_repository.get_invalid_item(index)