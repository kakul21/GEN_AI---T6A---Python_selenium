from os import name
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.selenium.dev/")
driver.maximize_window()
sleep(3)
driver.find_element(By.LINK_TEXT,"Downloads").click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"languages").click()
print(driver.title)
driver.close()