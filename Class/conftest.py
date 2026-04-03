import pytest

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = Chrome(options=o)
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    yield driver
    driver.close()