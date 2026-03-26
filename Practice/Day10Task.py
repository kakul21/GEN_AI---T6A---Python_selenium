from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)


## Task

import os
'''driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_")
driver.find_element(By.ID,"login-button").click()
expected = driver.current_url
actual = "https://www.saucedemo.com/inventory.html"
# assert expected == actual, "URL Unmatched"'''

# Method 1
'''if expected == actual:
    print("Login Successful")
else:
    folder = os.path.join(os.getcwd(), "Screenshot")
    os.makedirs(folder,exist_ok=True)
    driver.save_screenshot(f'{folder}/screenshot.png')'''

# Method 2
'''try:
    assert expected == actual, "Login Failed"
    print("Login Successful")
except:
    folder = os.path.join(os.getcwd(), "Screenshot")
    os.makedirs(folder, exist_ok=True)
    driver.save_screenshot(f'{folder}/screenshot.png')'''

actions = ActionChains(driver)

## Task1

'''
driver.get("https://in.pinterest.com/")
driver.maximize_window()
folder = os.path.join(os.getcwd(), "Screenshot")
os.makedirs(folder,exist_ok=True)
driver.save_screenshot(f'{folder}/screenshot_pinterest.png')
ele = driver.find_element(By.XPATH,'//img[@src="https://s.pinimg.com/webapp/group-boards-1px-c7997766.png"]')
actions.scroll_to_element(ele).pause(2).perform()
ele.screenshot(f'{folder}/screenshot_pinterest_2.png')
driver.close()
'''

## Task2
'''
driver.get("https://www.lenskart.com/")
driver.maximize_window()
driver.find_element(By.ID,"lrd1").click()
expected = "https://www.lenskart.com/eyeglasses.html"
actual = driver.current_url
assert expected == actual, "URL Unmatched"
dropdown = driver.find_element(By.ID,"sortByDropdown")
option = Select(dropdown)
option.select_by_visible_text('Most Viewed')
sleep(2)
folder = os.path.join(os.getcwd(),"Screenshot")
os.makedirs(folder,exist_ok=True)
driver.save_screenshot(f'{folder}/screenshot_lenskart.png')
driver.close()
'''

## Task 3
'''driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(5)
search=driver.find_element(By.ID,"twotabsearchtextbox")
search.send_keys("Laptop")
wait = WebDriverWait(driver, 10)
Fourth_suggestion=wait.until(EC.element_to_be_clickable((By.ID,"sac-suggestion-row-4")))
Fourth_suggestion.click()
driver.find_element(By.CLASS_NAME,"a-button-text.a-declarative").click()
driver.find_element(By.XPATH,"//a[text()='Newest Arrivals']").click()
driver.find_element(By.XPATH,"(//span[text()='Free Shipping'])").click()
product_name = driver.find_element(By.XPATH,'(//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"])[1]').text
product_price = driver.find_element(By.XPATH,"(//span[@class='a-price-whole'])[1]").text
print(product_name,":",product_price)
driver.close()'''