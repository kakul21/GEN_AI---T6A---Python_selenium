from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

## Task1 = In TestTaskDay1.py file 

## Task2
# open demowebshop website
# click apparel and shoes
# handle all three dropdowns

'''
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"(//a[@href='/apparel-shoes'])[1]").click()
dropdown1 = driver.find_element(By.ID,"products-orderby")
options = Select(dropdown1)
options.select_by_index(2)

dropdown2 = driver.find_element(By.ID,"products-pagesize")
options = Select(dropdown2)
options.select_by_visible_text("4")

dropdown3 = driver.find_element(By.ID,"products-viewmode")
options = Select(dropdown3)
options.select_by_index(1)
driver.close()
'''


## Task3
# Open demowebshop application
# Scroll to Facebook link (bottom of page)
# Click and enter username and password
# Click on login

'''driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element(By.XPATH,'//a[@href="http://www.facebook.com/nopCommerce"]').click()
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(10)
Email_or_username = driver.find_element(By.XPATH,'(//input[@name="email"])[2]')
Email_or_username.send_keys("ABC@gmail.com")
Password = driver.find_element(By.XPATH,'(//input[@name="pass"])[2]')
Password.send_keys("123456")
log_in = driver.find_element(By.XPATH,'//div[@class="x1ja2u2z x78zum5 x2lah0s x1n2onr6 xl56j7k x6s0dn4 xozqiw3 x1q0g3np x14ldlfn x1b1wa69 xws8118 x5fzff1 x972fbf x10w94by x1qhh985 x14e42zd x9f619 xpdmqnj x1g0dm76 xtvsq51 x1fq8qgq"]')
log_in.click()'''





