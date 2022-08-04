import requests


def test_option(get_params):
    request = requests.get(get_params[0])
    assert request.status_code == get_params[1]
