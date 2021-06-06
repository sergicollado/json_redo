import pytest
from unittest.mock import Mock
from infrastructure.message_client import MessageClient
from application_layer.json_processor import JsonProcessor
from infrastructure.processed_data_repository import ProcessedDataRepository


@pytest.fixture
def processed_repository():
    repository = ProcessedDataRepository()
    yield repository
    repository.data.clear()


@pytest.fixture
def message_client():
    return MessageClient

@pytest.fixture
def json_processor(message_client, processed_repository):
    return JsonProcessor(message_client, processed_repository)


@pytest.fixture
def preprocessed_json():
    filename = 'src/tests/fixtures/fixture_base.json'
    json_file = open(filename, "rb")
    yield json_file
    json_file.close()


@pytest.fixture
def to_process_json():
    filename = 'src/tests/fixtures/fixture_base_extended.json'
    json_file = open(filename, "rb")
    yield json_file
    json_file.close()


def test_should_save_index_of_already_process_data(preprocessed_json,
                                                   json_processor,
                                                   processed_repository):
    json_processor.process(preprocessed_json)

    expected_processed_range = 3

    for i in range(expected_processed_range):
        assert processed_repository.is_already_processed(i)


def test_processed_data_repository_should_return_false_if_ask_for_a_not_processed_data(
        preprocessed_json, json_processor, processed_repository):
    json_processor.process(preprocessed_json)
    expected_not_processed_index = 4
    is_processed = processed_repository.is_already_processed(
        expected_not_processed_index)
    assert not is_processed


def test_process_must_not_process_already_processed_data(
        to_process_json, json_processor, processed_repository):
    processed_repository.append(0)
    processed_repository.append(1)
    processed_repository.append(2)

    MessageClient.send_post = Mock()
    MessageClient.send_sms = Mock()
    MessageClient.send_email = Mock()
    json_processor.process(to_process_json)
    expected_post_data = {
        "name": "John Doe 4",
        "email": None,
        "phone": None,
        "url": "http: //example.com/push/4",
        "type": "post"
    }
    expected_email_data = {
        "name": "John Doe 5",
        "email": "doe@example.com5",
        "phone": None,
        "url": "http: //example.com",
        "type": "email"
    }
    expected_sms_data = {
        "name": "John Doe 6",
        "email": None,
        "phone": "+346920182646",
        "url": None,
        "type": "sms"
    }

    MessageClient.send_post.assert_called_once_with(expected_post_data['url'],
                                                    expected_post_data)
    MessageClient.send_sms.assert_called_once_with(expected_sms_data['phone'],
                                                    expected_sms_data)
    MessageClient.send_email.assert_called_once_with(expected_email_data['email'],
                                                    expected_email_data)