

from domain.validators.exceptions import BadParametersError


def test_BadParametersError_must_return_a_proper_message():
    expected_message=  "aClassName params: required_param_01 - required_param_02 not found, data: {'invalid': 'dict'}"
    try:
        raise BadParametersError('aClassName', ['required_param_01','required_param_02'], {'invalid':'dict'})
    except BadParametersError as e:
        assert e.message == expected_message
