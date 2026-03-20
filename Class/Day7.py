from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

# DropDowns - Select and Custom
#Select = HTML SELECT
#Custom = list div
'''<select>
<option>Dance</option>>
<option>Sing</option>
</select>'''

# Methods
# M1 = select_by_visible_text()
# M2 = select_by_index()
# M3 = select_by_value()

'''driver.get("file:///C:/Users/hp5cd/Downloads/E22_Dropdowns.html")
driver.maximize_window()
# dropdown = driver.find_element(By.ID,"state")
# option = Select(dropdown)
# option.select_by_visible_text("Maharastra")
# sleep(2)
# option.select_by_index(1) # Indexing starts from 0
# sleep(2)
# option.select_by_value("MH")

# We don't have deselect for single select

# Multiple Select Element
dropdown = driver.find_element(By.ID,"hobby")
option = Select(dropdown)
option.select_by_value("dance")
sleep(2)
option.select_by_index(3)
option.select_by_visible_text("Music")

#To deselect the element
# option.deselect_by_index(3)
# option.deselect_by_visible_text("Badminton")
option.deselect_all()'''

driver.get("https://www.amazon.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Shoes for men")
sleep(2)
list=driver.find_elements(By.CLASS_NAME,"s-suggestion-container")
for i in list:
    print(i.text)
sleep(2)
print(len(list))
list[2].click()
# driver.find_element(By.ID,"sac-suggestion-row-2").click()




