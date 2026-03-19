from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument("headless")
driver=Chrome(options=o)

'''
driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(10)
#driver.find_element(By.TAG_NAME,"a").click() ## First link on the page is fetched
links=driver.find_elements(By.TAG_NAME,"a")
print(links)

## To check no of anchor tags present on web page
print(len(links))

## To print the visible text of all anchor tags present
for i in links:
    print(i.text)

## To fetch nth number of element
links[2].click()
driver.close()
'''

'''
driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(10)
ele = driver.find_element(By.XPATH,'//a[@class="gb_A"]')
print(ele.get_attribute('aria-label'))
driver.close()
'''

'''driver.get("https://www.amazon.com")
driver.maximize_window()
driver.implicitly_wait(10)
links=driver.find_elements(By.XPATH,"//a[@class='nav-a  ']")
print(len(links))
for i in links:
    print(i.text,":",i.get_attribute('href'))
driver.close()
'''

# is_displayed() - If element is visible or not
# is_enabled() - If element is enable or not
# is_selected() - element is selected or not

'''
driver.get("https://www.facebook.com")
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH,'//div[@aria-label="Log in"]')
print(ele.is_displayed())
print(ele.is_enabled())
btn = driver.find_element(By.XPATH,'//input[@type="submit"]')
print(btn.is_displayed())
print(btn.is_enabled())
driver.close()
'''

'''driver.get("https://www.naukri.com/registration/createAccount?othersrcp=16201&err=1")
driver.maximize_window()
sleep(2)
btn = driver.find_element(By.XPATH,'//button[@type="submit"]')
print(btn.is_displayed())
print(btn.is_enabled())
driver.close()
'''

'''
driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()
checkbox1 = driver.find_element(By.XPATH,'//input[@type="checkbox"]')
print("checkbox1 is selected:",checkbox1.is_selected())
checkbox2 = driver.find_element(By.XPATH,'//input[@type="checkbox"][2]')
print("checkbox2 is selected:",checkbox2.is_selected())
driver.close()
'''

'''driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.find_element(By.ID,"firstName").send_keys("Chavi")
driver.find_element(By.ID,"lastName").send_keys("ABC")
driver.find_element(By.ID,"userEmail").send_keys("ABC@gmail.com")
driver.find_element(By.ID,"gender-radio-2").click()
driver.find_element(By.ID,"userNumber").send_keys("123")
driver.find_element(By.XPATH,"//input[@id='dateOfBirthInput']").click()
driver.find_element(By.XPATH,"//div[@aria-label='Choose Friday, March 20th, 2026']").click()
driver.find_element(By.ID,"hobbies-checkbox-3").click()
driver.find_element(By.ID,"uploadPicture").send_keys(r"C:\Users\hp5cd\Desktop\practice\muff.jpeg")'''

'''driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.ID,"singleFileInput").send_keys(r"C:\Users\hp5cd\Desktop\IT\Bracelet - Copy.jpg")
## How to add multiple files - M1

# driver.find_element(By.ID,"multipleFilesInput").send_keys(r"C:\Users\hp5cd\Desktop\IT\Flower Pot (1).jpg")
# driver.find_element(By.ID,"multipleFilesInput").send_keys(r"C:\Users\hp5cd\Desktop\IT\Bracelet - Copy.jpg")
# driver.find_element(By.ID,"multipleFilesInput").send_keys(r"C:\Users\hp5cd\Desktop\IT\Reusable Cup.jpg")
## How to add multiple files - M2

list = [r"C:\Users\hp5cd\Desktop\IT\Flower Pot (1).jpg",r"C:\Users\hp5cd\Desktop\IT\Bracelet - Copy.jpg",r"C:\Users\hp5cd\Desktop\IT\Reusable Cup.jpg"]
for i in list:
    driver.find_element(By.ID,"multipleFilesInput").send_keys(i)
#driver.close()'''






