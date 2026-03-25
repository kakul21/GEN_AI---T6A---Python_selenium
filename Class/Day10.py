from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

## Assert - Syntax: assert condition , msg displayed when condition fails
## Example - assert expected == actual , "Title Mismatch"

'''driver.get("https://google.com")
driver.maximize_window()
# print(driver.title)
expected = "Google"
actual = driver.title
assert expected == actual , "Title Mismatch"
# if actual result is not equal to expected result then AssertionError will be there
driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys("Hello")
driver.close()'''

'''driver.get("https://amazon.com")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//a[@href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]').click()
actual = "Amazon.com Best Sellers: The most popular items on Amazon"
expected = driver.title
assert expected == actual , "Title Mismatch"
print(actual)'''

'''import os
## Screenshot

                                                ## For whole page

driver.get("https://google.com")
driver.maximize_window()
# driver.save_screenshot("google.png")
folder = os.path.join(os.getcwd(), "screenshot")
os.makedirs(folder,exist_ok=True)
# driver.save_screenshot(f'{folder}/screenshot_page.png')
# driver.close()

                                            ## For particular element

# ele = driver.find_element(By.XPATH,"//textarea[@title='Search']")
# ele.screenshot(f'{folder}/screenshot_ele.png')
# driver.close()

# ele = driver.find_element(By.ID,"LS8OJ")
# ele.screenshot(f'{folder}/screenshot_ele2.png')
# driver.close()

import time
ele = driver.find_element(By.ID,"LS8OJ")
timestamp = time.strftime("%Y%m%d-%H%M%S")
ele.screenshot(f'{folder}/screenshot_ele2_{timestamp}.png')
driver.close()'''











