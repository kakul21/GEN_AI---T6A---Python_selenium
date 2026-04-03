import pytest
from Pyxl_fetch import get_test_data

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("username,password",get_test_data())
def test_login(driver,username,password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url, "Invalid Credentials"



