import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser..')
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait
