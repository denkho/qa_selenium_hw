import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument('--start-maximized')
    # options.add_argument('--disable-extensions')
    # options.add_argument('--headless')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    print('\nquit browser..')
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait
