from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

actions = ActionChains(driver)

## Task1
# Mouse Hover action on Automation testing website
# Double click on copy text
# Drag and drop

'''driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)
Hover = driver.find_element(By.CLASS_NAME,"dropbtn")
actions.move_to_element(Hover).perform()
Double_click = driver.find_element(By.XPATH,"//button[text()='Copy Text']")
actions.double_click(Double_click).perform()
drag = driver.find_element(By.ID,"draggable")
drop = driver.find_element(By.ID,"droppable")
actions.drag_and_drop(drag,drop).perform()
driver.close()'''

## Task2
# Launch Nike
# Perform mouse hover on kids and after sometime click on kids
# Scroll and click on shop
# scroll to one shoe and click
# Select size and add to cart

'''driver.get("https://www.nike.in/")
driver.maximize_window()
driver.implicitly_wait(10)
Kids_section = driver.find_element(By.XPATH,"//span[text()='Kids']")
actions.move_to_element(Kids_section).perform()
Kids_section.click()
driver.switch_to.window(driver.window_handles[1])
Shop_btn = driver.find_element(By.CLASS_NAME,"css-1g841a0")
actions.scroll_to_element(Shop_btn).pause(3).perform()
sleep(2)
Shop_btn.click()
driver.switch_to.window(driver.window_handles[1])
shoe = driver.find_element(By.XPATH,"(//div[@class='css-1sjxv95'])[14]")
actions.scroll_to_element(shoe).perform()
sleep(2)
shoe.click()
driver.switch_to.window(driver.window_handles[2])
size = driver.find_element(By.XPATH,"//label[text()='UK 4.5']")
size.click()
add_to_cart = driver.find_element(By.XPATH,"//button[text()='Add to Bag']")
add_to_cart.click()
driver.close()'''

## Task3
# open flipkart
# perform scroll actions
# scroll to myntra and click myntra
# go back
# click shopsy
# all three needs to be clicked
# For all three - print id,title,url

'''driver.get("https://www.flipkart.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,"b3wTlE").click()
Myntra = driver.find_element(By.XPATH,"//a[@href='https://www.myntra.com/']")
actions.scroll_to_element(Myntra).perform()
sleep(2)
Myntra.click()
driver.switch_to.window(driver.window_handles[1])
sleep(2)
print("Current ID:",driver.current_window_handle)
print("Current Title:",driver.title)
print("Current URL:",driver.current_url)
sleep(2)
driver.switch_to.window(driver.window_handles[0])
Cleartrip = driver.find_element(By.XPATH,"//a[@href='https://www.cleartrip.com/']")
actions.scroll_to_element(Cleartrip).perform()
sleep(2)
Cleartrip.click()
driver.switch_to.window(driver.window_handles[2])
sleep(2)
print("Current ID:",driver.current_window_handle)
print("Current Title:",driver.title)
print("Current URL:",driver.current_url)
sleep(2)
driver.switch_to.window(driver.window_handles[0])
Shopsy = driver.find_element(By.XPATH,"//a[@href='https://www.shopsy.in']")
actions.scroll_to_element(Shopsy).perform()
sleep(2)
Shopsy.click()
driver.switch_to.window(driver.window_handles[3])
sleep(2)
print("Current ID:",driver.current_window_handle)
print("Current Title:",driver.title)
print("Current URL:",driver.current_url)
driver.close()'''
