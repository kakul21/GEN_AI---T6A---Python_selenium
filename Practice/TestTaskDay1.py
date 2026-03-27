from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

def test_launching():
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()

def test_registering():
    register=driver.find_element(By.XPATH,"//a[text()='Register']")
    register.click()

def test_gender():
    gender = driver.find_element(By.ID,"gender-female")
    gender.click()

def test_firstname():
    firstname = driver.find_element(By.ID,"FirstName")
    firstname.send_keys("John")

def test_lastname():
    lastname = driver.find_element(By.ID,"LastName")
    lastname.send_keys("Doe")

def test_email():
    email = driver.find_element(By.ID,"Email")
    email.send_keys("John@gmail.com")

def test_password():
    password = driver.find_element(By.ID,"Password")
    password.send_keys("12345")

def test_confirm_password():
    confirm_password = driver.find_element(By.ID,"ConfirmPassword")
    confirm_password.send_keys("12345")

def test_register_button():
    register_button = driver.find_element(By.ID,"register-button")
    register_button.click()