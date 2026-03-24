from operator import index
from time import sleep
from tokenize import tabsize

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

# Task1
'''driver.get("https://x.com/")
driver.maximize_window()
switch = driver.find_element(By.XPATH,"//iframe[@title='Sign in with Google Button']")
driver.switch_to.frame(switch)
sign = driver.find_element(By.XPATH,"//span[text()='Sign up with Google']")
sign.click()
driver.close()'''

# Task2
'''driver.get("https://www.zomato.com/login")
driver.maximize_window()
driver.switch_to.frame(0)
switch=driver.find_element(By.XPATH,"(//iframe[@title='Sign in with Google Button'])[1]")
driver.switch_to.frame(switch)
driver.find_element(By.XPATH,"//span[text()='Sign in with Google']").click()
driver.close()'''

# Task3
# Open 3 websites in separate tab
# Fetch title,url,id
# close all tabs except the first one

'''driver.get("https://x.com/")
driver.maximize_window()
print("Current ID:",driver.current_window_handle)
print("Current Title:",driver.title)
print("Current URL:",driver.current_url)
driver.switch_to.new_window()
driver.get("https://amazon.com/")
driver.switch_to.window(driver.window_handles[1])
print("Current ID:",driver.current_window_handle)
print("Current Title:",driver.title)
print("Current URL:",driver.current_url)
driver.switch_to.new_window()
driver.get("https://flipkart.com/")
print("Current ID:",driver.current_window_handle)
print("Current Title:",driver.title)
print("Current URL:",driver.current_url)
driver.close()
driver.switch_to.window(driver.window_handles[1])
driver.close()'''

# Task4
# open internetheroku
# javascript alerts and fetch text

'''driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print("Text appears for first alert:",alert.text)
alert.accept()
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
alert = driver.switch_to.alert
print("Text appears for second alert:",alert.text)
alert.dismiss()
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
alert = driver.switch_to.alert
alert.send_keys("Hello")
print("Text appears for third alert:",alert.text)
alert.accept()
driver.close()'''







