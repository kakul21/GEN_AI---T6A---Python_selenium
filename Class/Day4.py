from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument('--headless') # browser doesn't get open but actions are done
driver = Chrome(options=o)

# Traversing
## Forward and Backward

'''driver.get("https://demoqa.com/webtables")
driver.maximize_window()
sleep(2)
salary = driver.find_element(By.XPATH,"//td[text()='Cierra']/..//td[5]")
print(salary.text)
department = driver.find_element(By.XPATH,"//td[text()='Kierra']/..//td[6]")
print("Department:",department.text)
driver.close()'''

'''driver.get("https://the-internet.herokuapp.com/tables")
driver.maximize_window()
sleep(2)
due = driver.find_element(By.XPATH,"//td[text()='Frank']/../td[4]")
print("DueAmount:",due.text)
driver.close()'''

## Following and preceding sibling

'''driver.get("https://the-internet.herokuapp.com/tables")
driver.maximize_window()
sleep(2)
due = driver.find_element(By.XPATH,"//td[text()='Tim']//following-sibling::td[2]")
print("DueAmount:",due.text)
driver.close()'''

'''driver.get("https://www.amazon.com/")
driver.maximize_window()
sleep(3)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("mobiles")
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)
#driver.find_element(By.CLASS_NAME,"a-link-normal.s-line-clamp-4.s-link-style.a-text-normal").click()
#price = driver.find_element(By.XPATH,"//span[contains(text(),'Samsung Galaxy S26')]/../../../..//span[@class='a-price-whole']")
price = driver.find_element(By.XPATH,"//span[contains(text(),'Samsung Galaxy S25')]/../../../..//span[@class,'a-price-whole']")
#driver.find_element(By.XPATH,"//span[contains(text(),'Samsung Galaxy S25')]/../../../../div[1]//div[2]").click()
sleep(2)
print("Price:$",price.text)
driver.close()'''

'''driver.get("https://www.flipkart.com")
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME,"b3wTlE").click()
sleep(2)
driver.find_element(By.CLASS_NAME,"nw1UBF.v1zwn25").send_keys("Watch")
sleep(2)
driver.find_element(By.CLASS_NAME,"XFwMiH").click()
#price=driver.find_element(By.XPATH,"(//div[contains(text(),'PRAIZY')]/..//div)[5]")
price=driver.find_element(By.XPATH,"(//div[contains(text(),'ABREXO')]/..)/a/div/div")
Name=driver.find_element(By.XPATH,"(//div[contains(text(),'ABREXO')]/..)//a")
print("Name:",Name.text,"Price:",price.text)
Hotdeal = driver.find_element(By.XPATH,"(//div[contains(text(),'ABREXO')]/..)//div[4]")
print("Hotdeal:",Hotdeal.text=="Hot Deal")
driver.close()'''

