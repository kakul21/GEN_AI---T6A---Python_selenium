import pytest

## we can apply fixture for one function
'''@pytest.fixture
def greet():
    print("Hello all!")
    yield
    print("Good bye")

def test_morning(greet):
    print("Hello morning!")

def test_evening():
    print("Hello evening!")'''

## we can apply fixtures to all the functions using "@pytest.fixture(autouse=True)"
'''@pytest.fixture(autouse=True)
## for fixture it should not be test as usually we give it as "def setup"
def greet():
    print("Hello all!")
    yield
    print("Good bye")

def test_morning():
    print("Hello morning!")

def test_evening():
    print("Hello evening!")'''

'''from selenium.webdriver import Chrome, ChromeOptions
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

@pytest.mark.parametrize("username,password",[
    ("standard_user","secret_sauce"),
    ("locked_out_user","secret_sauce"),
    ("problem_user","secret_sauce"),
    ("performance_glitch_user","secret_sauce"),
    ("error_user","secret_sauce"),
])

def test_login(driver,username,password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url, "Invalid Credentials"'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
@pytest.fixture
def setup():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = Chrome(options=o)
    driver.get("https://demowebshop.tricentis.com/register")
    driver.maximize_window()
    sleep(2)
    yield driver
    driver.close()

class Test:

    def test_gender(self,setup):
        gender = setup.find_element(By.ID, "gender-female")
        gender.click()

    def test_firstname(self,setup):
        firstname = setup.find_element(By.ID, "FirstName")
        firstname.send_keys("John")

    def test_lastname(self,setup):
        lastname = setup.find_element(By.ID, "LastName")
        lastname.send_keys("Doe")

    def test_email(self,setup):
        email = setup.find_element(By.ID, "Email")
        email.send_keys("John@gmail.com")

    def test_password(self,setup):
        password = setup.find_element(By.ID, "Password")
        password.send_keys("12345")

    def test_confirm_password(self,setup):
        confirm_password = setup.find_element(By.ID, "ConfirmPassword")
        confirm_password.send_keys("12345")

    def test_register_button(self,setup):
        register_button = setup.find_element(By.ID, "register-button")
        register_button.click()




