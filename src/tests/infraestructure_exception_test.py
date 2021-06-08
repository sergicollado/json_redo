
from infrastructure.exceptions import PersistenceFileError


def test_PersistenceFileError_must_return_a_proper_message():
    expected_message=  "Error Reading or Writing file: filename.json <class 'FileNotFoundError'>"
    try:
        raise PersistenceFileError('filename.json', FileNotFoundError)
    except PersistenceFileError as e:
        assert e.message == expected_message
