from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

# Task 1
'''driver.get('https://www.amazon.com')
driver.maximize_window()
print(driver.title)'''

# Task 2
'''driver.get('https://www.amazon.com')
driver.maximize_window()
print(driver.current_url)'''

# Task 3
'''driver.get("https://www.wikipedia.com")
driver.maximize_window()
driver.refresh()
print(driver.title)
print(driver.current_url)
driver.get('https://amazon.com')
sleep(5)
print(driver.title)
print(driver.current_url)
sleep(5)
driver.close()'''
