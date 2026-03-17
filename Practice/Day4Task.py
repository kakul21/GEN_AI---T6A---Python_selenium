from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

# Task1
'''driver.get("https://www.amazon.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("mobile phones")
sleep(2)
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)
price=driver.find_element(By.XPATH,"(//span[contains(text(),'Samsung Galaxy A16 4G LTE')]/../../../..//span[@class='a-color-base'])")
print(price.text)
driver.close()'''

# Task2
'''driver.get("https://www.flipkart.com")
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME,"b3wTlE").click()
driver.find_element(By.XPATH,"//input[@placeholder='Search for Products, Brands and More']").send_keys("Watches")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
price = driver.find_element(By.XPATH,"(//div[contains(text(),'PROVOGUE')]//..//div)[4]/div")
print(price.text)
driver.close()'''
