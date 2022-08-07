import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru")
    parser.addoption("--status_code", action="store", default=200)


@pytest.fixture(scope='session')
def get_params(request):
    url = request.config.getoption("--url")
    status_code = request.config.getoption("--status_code")
    return url, status_code
