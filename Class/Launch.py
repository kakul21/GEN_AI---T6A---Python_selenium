from time import sleep
'''from selenium.webdriver import Chrome
driver = chrome()
sleep(5)'''

'''from time import sleep
from selenium.webdriver import Edge
driver = Edge()
sleep(5)'''

from  selenium.webdriver import Chrome,ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

'''## To open a web page
driver.get('https://google.com')

## To maximize web page
driver.maximize_window()

## To minimize web page
driver.minimize_window()

## return type is None - get,maximize,minimize

# To open web page in fullscreen 
driver.fullscreen_window()'''

# Browser Methods
'''from time import sleep
driver.get('https://amazon.com')
driver.maximize_window()
sleep(5)
driver.minimize_window()
sleep(5)
driver.fullscreen_window()
sleep(5)'''

# Page Information Properties
## To fetch the Title
'''driver.get('https://google.com')
title = driver.title # title is the property
print(title)'''

# return type = string

## To fetch Current URL
#print(driver.current_url)
## To get the content of the HTML file
#print(driver.page_source)

driver.get('https://amazon.com')
driver.maximize_window()
sleep(5)
title = driver.title
print(title)
#print(driver.current_url)
# To check Browser name
name = driver.name
#print(name)
#sleep(5)
#driver.close() # only the tab opened through this is close  (current tab gets close)
#driver.quit() # all the tabs gets close (closing entire browsing window)

driver.back()
sleep(8)
driver.forward()
sleep(5)
driver.refresh()



