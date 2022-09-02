import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption("--url", action="store", default='http://192.168.1.76:8081')


@pytest.fixture(scope='module')
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == 'Chrome':
        _driver = webdriver.Chrome()
    elif browser == 'Firefox:':
        _driver = webdriver.Firefox()
    elif browser == 'Opera':
        _driver = webdriver.Opera()
    else:
        raise pytest.UsageError("--browser_name should be Chrome or Firefox or Opera")
    _driver.implicitly_wait(3)
    _driver.get(request.config.getoption("--url"))
    yield _driver
    _driver.quit()
