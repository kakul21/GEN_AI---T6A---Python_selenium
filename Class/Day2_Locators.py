from os import name
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)


'''driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(5)
#driver.find_element(By.ID,"userName").send_keys("Hello")
username = driver.find_element(By.ID,"userName")
username.send_keys("Hello")
Email = driver.find_element(By.ID,"userEmail")
Email.send_keys("ABC@gmail.com")
Address = driver.find_element(By.ID,"currentAddress")
Address.send_keys("123456")
PerAddress = driver.find_element(By.ID,"permanentAddress")
PerAddress.send_keys("123456")
driver.find_element(By.ID,"submit").click()
driver.close()'''

'''driver.get("https://amazon.com")
driver.maximize_window()
sleep(5)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Shoes")
sleep(5)
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.close()'''

'''driver.get("https://www.facebook.com/")    
driver.maximize_window()
sleep(5)
driver.find_element(By.NAME,"email").send_keys("hello")
driver.close()'''

'''driver.get("https://amazon.com")
driver.maximize_window()
sleep(5)
# Compound classname should be written with "." in between
# If multiple elements are there with same class name then it should serve as first come, first served basis

driver.find_element(By.CLASS_NAME,"nav-input.nav-progressive-attribute").send_keys("Shoes")
sleep(5)
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.find_element(By.CLASS_NAME,"nav-cart-icon.nav-sprite").click()
driver.close()'''

'''driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(3)
driver.find_element(By.TAG_NAME,"input").send_keys("Hello")
sleep(3)
driver.find_element(By.TAG_NAME,"textarea").send_keys("123456")
sleep(3)
driver.find_element(By.CLASS_NAME,"btn.btn-primary").click()
driver.close()'''

# Link Text will work for anchor tags only
'''driver.get("https://www.amazon.in")
driver.maximize_window()
sleep(5)
driver.find_element(By.LINK_TEXT,"Mobiles").click()
driver.close()'''

'''driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT,"Kitchen").click()
sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT,"&").click()
driver.close()'''

'''driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
driver.find_element(By.CSS_SELECTOR,'input[placeholder="Search Amazon.in"]').send_keys("Hoodies")
sleep(2)
driver.find_element(By.ID,"nav-search-submit-button").click()'''



