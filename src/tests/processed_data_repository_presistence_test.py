import pytest
import os
from infrastructure.processed_data_repository_persistence import ProcessedDataRepositoryPersistence

file = 'processed_data.json'

@pytest.fixture
def repository():
    yield ProcessedDataRepositoryPersistence(file)
    os.remove(file) 

def test_repository_must_save_processed_data_after_call_save_method(repository: ProcessedDataRepositoryPersistence):
    repository.append(0)
    repository.append(1)
    repository.append(2)
    repository.save()

    other_repository_instance = ProcessedDataRepositoryPersistence(file)

    assert other_repository_instance.is_already_processed(0)
    assert other_repository_instance.is_already_processed(1)
    assert other_repository_instance.is_already_processed(2)


def test_repository_must_save_invalid_data_after_call_save_method(repository: ProcessedDataRepositoryPersistence):
    repository.append(0)
    repository.append(1)
    repository.append(2)
    repository.append_invalid_item(1, {'invalid': 1})
    repository.append_invalid_item(2,  {'invalid': 2})
    repository.save()

    other_repository_instance = ProcessedDataRepositoryPersistence(file)

    assert other_repository_instance.is_already_processed(0)
    assert other_repository_instance.is_already_processed(1)
    assert other_repository_instance.is_already_processed(2)

    invalid_item_01 = other_repository_instance.get_invalid_item(1)
    invalid_item_02 = other_repository_instance.get_invalid_item(2)
    assert invalid_item_01['data'] ==  {'invalid': 1}
    assert invalid_item_02['data'] ==  {'invalid': 2}

def test_repository_must_return_false_index_is_not_processed(repository: ProcessedDataRepositoryPersistence):
    repository.append(0)
    repository.save()

    other_repository_instance = ProcessedDataRepositoryPersistence(file)
    assert not other_repository_instance.is_already_processed(1)

def test_repository_must_return_invalid_items(repository: ProcessedDataRepositoryPersistence):
    repository.append(0)
    repository.append(1)
    repository.append(2)
    repository.append_invalid_item(1, {'invalid': 1})
    repository.append_invalid_item(2,  {'invalid': 2})
    repository.save()

    other_repository_instance = ProcessedDataRepositoryPersistence(file)

    assert other_repository_instance.is_already_processed(0)
    assert other_repository_instance.is_already_processed(1)
    assert other_repository_instance.is_already_processed(2)
    invalid_items = other_repository_instance.get_invalid_items()

    invalid_item_01 = invalid_items[0]
    invalid_item_02 = invalid_items[1]
    assert invalid_item_01['data'] ==  {'invalid': 1}
    assert invalid_item_02['data'] ==  {'invalid': 2}