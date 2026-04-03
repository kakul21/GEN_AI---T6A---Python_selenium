import pytest

## Task 1
# 1. open saucedemo website
# 2. using parametrize marker give username and password
# 3. Try to log in

@pytest.mark.parametrize("username,password",[
    ("standard_user","secret_sauce"),
    ("locked_out_user","secret_sauce"),
    ("problem_user","secret_sauce"),
    ("performance_glitch_user","secret_sauce"),
    ("error_user","secret_sauce"),
    ("project_user","secret_sauce"),
])

def test_registering(username,password):
    from selenium.webdriver import Chrome, ChromeOptions
    from selenium.webdriver.common.by import By
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = Chrome(options=o)
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()
    assert "inventory" in driver.current_url
    driver.close()
