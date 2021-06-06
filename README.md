# json_redo


## Installation

- Python 3.8

- This project use pipenv to manage the requeriments, check this link to install it:
https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv

- After that you can install python library packages:
  
```bash
# from the project root
# activated virtual env
pipenv shell
# install dependencies
pipenv install
# install dev dependencies if it needs
pipenv install --dev

```

## how to run

Execute app.py

```python
    python src/app.py

```

## Folder structure

```python
src                     # source code
src/domain              # core domain
src/infraestructure     # infraestructure layer
src/application_layer   # application layer
```

## Run Tests

```bash
# from the root of project
pytest

# test with coverage
pytest --cov=src src/

```

## Coverage


```bash
----------- coverage: platform linux, python 3.8.5-final-0 -----------
Name                                                      Stmts   Miss  Cover
-----------------------------------------------------------------------------
src/app.py                                                   11     11     0%
src/application_layer/__init__.py                             1      0   100%
src/application_layer/json_processor.py                      27      0   100%
src/domain/__init__.py                                        0      0   100%
src/domain/message_client_abstract.py                         9      0   100%
src/domain/notification_sender_abstract.py                    5      0   100%
src/domain/notification_sender_factory.py                    32      0   100%
src/domain/notification_types.py                              5      0   100%
src/domain/processed_data_repository_abstract.py             11      0   100%
src/domain/validators/__init__.py                             3      0   100%
src/domain/validators/abstract_classes.py                    14      0   100%
src/domain/validators/email_notification_validator.py         6      0   100%
src/domain/validators/exceptions.py                           6      1    83%
src/domain/validators/general_notification_validator.py       6      0   100%
src/domain/validators/post_notification_validator.py          6      0   100%
src/domain/validators/sms_notification_validator.py           6      0   100%
src/infraestructure/message_client.py                         8      0   100%
src/infraestructure/processed_data_repository.py             14      0   100%
src/tests/__init__.py                                         0      0   100%
src/tests/exceptions_validation_test.py                      15      0   100%
src/tests/json_processor_replay_test.py                      52      0   100%
src/tests/json_processor_test.py                             34      0   100%
src/tests/json_processor_validation_test.py                  48      0   100%
src/tests/message_client_test.py                              4      0   100%
-----------------------------------------------------------------------------
TOTAL                                                       323     12    96%
```