from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
'''driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#userName").send_keys("Hello")
driver.find_element(By.CSS_SELECTOR,".btn.btn-primary").click()
sleep(2)
driver.close()'''

#//input[@placeholder="Full Name"]
'''driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@placeholder='Full Name']").send_keys("ABC")
driver.find_element(By.XPATH,"//input[@placeholder='name@example.com']").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"//textarea[@placeholder='Current Address']").send_keys("1234")
driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']").send_keys("12345")
sleep(2)
driver.find_element(By.XPATH,"//button[text()='Submit']").click()
sleep(2)
driver.close()'''

#XPATH using attribute and text
'''driver.get("https://www.amazon.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//span[text()='Home Storage']").click()
sleep(2)
driver.find_element(By.XPATH,"//span[.='SNSLXH 5 Pack Stackable Closet Storage Basket, Multifunctional & Foldable Closet Organizer for Bathroom Kitchen Laundry Room Wardrobe Storage, Space-Saving Clothes Storage Drawer Organizer, White']").click()
sleep(2)
driver.find_element(By.XPATH,"//a[.=' Add to List ']").click()
driver.close()'''

#XPATH using contains attribute and contains text
driver.get("https://www.amazon.com/")
driver.maximize_window()
sleep(2)
#driver.find_element(By.XPATH,"//a[contains(text(),'Manage Your Content and Devices')]").click()
sleep(2)
#driver.find_element(By.XPATH, "//a[contains(@class,'nav_a')]").click()
##driver.find_element(By.XPATH,"(//a[contains(@class,'nav-a')])[1]").click()
driver.close()




