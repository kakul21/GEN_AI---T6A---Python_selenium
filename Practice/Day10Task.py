from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

import os
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_")
driver.find_element(By.ID,"login-button").click()
expected = driver.current_url
actual = "https://www.saucedemo.com/inventory.html"
# assert expected == actual, "Login Failed"

# Method 1
'''if expected == actual:
    print("Login Successful")
else:
    folder = os.path.join(os.getcwd(), "Screenshot")
    os.makedirs(folder,exist_ok=True)
    driver.save_screenshot(f'{folder}/screenshot.png')'''

# Method 2
'''try:
    assert expected == actual, "Login Failed"
    print("Login Successful")
except:
    folder = os.path.join(os.getcwd(), "Screenshot")
    os.makedirs(folder, exist_ok=True)
    driver.save_screenshot(f'{folder}/screenshot.png')'''



