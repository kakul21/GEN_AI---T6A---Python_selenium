from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

#Task1
'''driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,"b3wTlE").click()
driver.find_element(By.CLASS_NAME,"nw1UBF.v1zwn25").send_keys("Mobile")
driver.find_element(By.CLASS_NAME,"XFwMiH").click()
wait = WebDriverWait(driver,10)
Mobilename = wait.until(EC.visibility_of_element_located((By.XPATH,"(//div[@class='RG5Slk'])[6]"))).text
print(Mobilename)
driver.close()'''

#Task2
'''driver.get("https://demoqa.com/webtables")
driver.maximize_window()
wait = WebDriverWait(driver,10)
driver.find_element(By.ID,"addNewRecordButton").click()
driver.find_element(By.ID,"firstName").send_keys("Ansh")
driver.find_element(By.ID,"lastName").send_keys("Khatod")
driver.find_element(By.ID,"userEmail").send_keys("Ansh@gmail.com")
driver.find_element(By.ID,"age").send_keys("22")
driver.find_element(By.ID,"salary").send_keys("500000")
driver.find_element(By.ID,"department").send_keys("Technical")
driver.find_element(By.ID,"submit").click()
name = driver.find_element(By.XPATH,"//td/../..//tr[4]//td").text
salary = wait.until(EC.visibility_of_element_located((By.XPATH,"//td[.='Ansh']/../td[5]"))).text
print(name,":",salary)
driver.close()'''