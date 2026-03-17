from time import sleep
import time
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

#Implicit Wait

'''driver.get("https://www.decathlon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//a[@href='https://www.decathlon.in/shop/bags-and-backpacks']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//a[@href='https://www.decathlon.in/c/travel-bags-and-duffle-bags-26122']").click()
driver.close()'''

# Explicit Wait

'''driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[.='Start']").click()
#h = driver.find_element(By.XPATH,"//div[@id='start']//following-sibling::div/h4")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='finish']"))).click()
txt = driver.find_element(By.XPATH,"//div[@id='finish']").text
#h=driver.find_element(By.XPATH,"//h4[.='Hello World!']")
# sleep(5)
print(txt)
driver.close()'''





