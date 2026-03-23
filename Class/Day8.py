from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

actions = ActionChains(driver)

# Keys.ENTER
'''driver.get("https://amazon.in")
driver.maximize_window()
driver.implicitly_wait(10)
search = driver.find_element(By.ID,"twotabsearchtextbox")
search.send_keys("Watches")
search.send_keys(Keys.ENTER)
driver.close()'''

# Keys.CONTROL
'''driver.get("https://demoqa.com/text-box")
driver.maximize_window()
Current_address=driver.find_element(By.ID,"currentAddress")
Current_address.send_keys("gyugyugfuiguigui")
Current_address.send_keys(Keys.CONTROL,'A')
Current_address.send_keys(Keys.CONTROL,'C')
Permanent_address = driver.find_element(By.ID,"permanentAddress")
Permanent_address.send_keys(Keys.CONTROL,'V')
driver.close()'''

actions = ActionChains(driver)

# Double_click, Single_click, Right_click
'''driver.get("https://demoqa.com/buttons")
driver.maximize_window()
driver.implicitly_wait(10)
double_clickk = driver.find_element(By.ID,"doubleClickBtn")
actions.double_click(double_clickk).perform()
single_clickk = driver.find_element(By.XPATH,"//button[text()='Click Me']")
actions.click(single_clickk).perform()
# # We are rewriting same script again as sometimes the script won't click anything due to ads or something
# actions.click(single_clickk).perform()
# actions.double_click(double_clickk).perform()
right_click = driver.find_element(By.ID,"rightClickBtn")
actions.context_click(right_click).perform()
driver.close()'''

# scroll_to_element
'''driver.get("https://amazon.com/")
driver.maximize_window()
sleep(3)
About = driver.find_element(By.XPATH,"//a[@href='https://www.aboutamazon.com/?utm_source=gateway&utm_medium=footer']")
actions.scroll_to_element(About).pause(3).perform()
actions.click(About).perform()
driver.close()'''

# scroll_by_amount
'''driver.get("https://amazon.com/")
driver.maximize_window()
sleep(3)
About = driver.find_element(By.XPATH,"//a[@href='https://www.aboutamazon.com/?utm_source=gateway&utm_medium=footer']")
actions.scroll_by_amount(0,2000).pause(3).perform()
actions.click(About).perform()
driver.close()'''

# scroll_from_origin
'''driver.get("https://amazon.com/")
driver.maximize_window()
sleep(3)
About = driver.find_element(By.XPATH,"//a[@href='https://www.aboutamazon.com/?utm_source=gateway&utm_medium=footer']")
o = ScrollOrigin.from_element(About)
# o= ScrollOrigin.from_viewport(0,1500)
actions.scroll_from_origin(o,0,1000).perform()
driver.close()'''

# moveToElement
'''driver.get("https://amazon.com/")
driver.maximize_window()
driver.implicitly_wait(10)
ele = driver.find_element(By.ID,"nav-hamburger-menu")
actions.move_to_element(ele).perform()
driver.close()'''

# click_and_hold
'''driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
driver.maximize_window()
driver.implicitly_wait(10)
password = driver.find_element(By.ID,"password")
# actions.click_and_hold(password).perform()
actions.click_and_hold(password).pause(1).release().perform()
driver.close()'''

# Drag and Drop
'''driver.get("https://demoqa.com/droppable")
driver.maximize_window()
driver.implicitly_wait(10)
drag_element = driver.find_element(By.ID,"draggable")
drop_element = driver.find_element(By.ID,"droppable")
sleep(4)
actions.drag_and_drop(drag_element,drop_element).perform()
driver.close()'''

## Actionchains done

# Window switching or tab switching / Handling Multiple window

# 1. current_window_handle
# 2. window_handles
# 3. switch_to_window

'''driver.get("https://google.com/")
driver.maximize_window()
sleep(5)
print(driver.title)
# Manually Opening three tabs
driver.switch_to.new_window('tab')
driver.get("https://demoqa.com/")
current=driver.current_window_handle
print(current)
print(driver.title)
all = driver.window_handles
# print(all)
for i in all:
    print(i)
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.ID,"APjFqb").send_keys("Hello")
driver.close()'''
