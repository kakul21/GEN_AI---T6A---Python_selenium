from os import name
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
driver.find_element(By.ID,"nav-global-location-popover-link").click()
sleep(2)
driver.close()'''

# Task2
'''driver.get("https://www.facebook.com")
driver.maximize_window()
sleep(2)
driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
sleep(2)
driver.find_element(By.NAME,"pass").send_keys("1234")
sleep(2)
#driver.find_element(By.CLASS_NAME,"html-div.xdj266r.xat24cr.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x6s0dn4.x78zum5.xl56j7k.x1e0frkt.xf0ucvx.xx2axb6").click()
driver.close()'''

# Task3
'''driver.get("https://www.amazon.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Mobiles")
sleep(2)
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"samsung").click()
driver.close()'''

# Task4
'''driver.get("https://www.selenium.dev/")
driver.maximize_window()
sleep(3)
driver.find_element(By.LINK_TEXT,"Downloads").click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"languages").click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"Register").click()
sleep(2)
print(driver.title)
driver.close()
'''

