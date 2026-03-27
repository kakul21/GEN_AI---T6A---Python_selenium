from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

## Task1
# open demowebshop website
# click apparel and shoes
# handle all three dropdowns

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

