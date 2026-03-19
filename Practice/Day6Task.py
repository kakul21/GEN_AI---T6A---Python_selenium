from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument("headless")
driver=Chrome(options=o)

# Task1
'''driver.get("https://www.amazon.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Headphones")
driver.find_element(By.ID,"nav-search-submit-button").click()
items = driver.find_elements(By.XPATH,"//div[@class='puis-card-container s-card-container s-overflow-hidden aok-relative desktop-list-view puis-include-content-margin puis puis-v2zbw063pqfq572g06vyx3q3f16 s-latency-cf-section puis-card-border']")
print(items)
print(len(items))
items[4].click()
driver.close()'''

# Task2
'''driver.get("https://www.amazon.com")
driver.maximize_window()
driver.implicitly_wait(10)
links=driver.find_elements(By.XPATH,"//a[@class='nav-a  ']")
print(len(links))
for i in links:
    print(i.text,":",i.get_attribute('href'))
driver.close()'''

# Task3
'''driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
driver.find_element(By.ID,"gender-female").click()
driver.find_element(By.ID,"FirstName").send_keys("John")
driver.find_element(By.ID,"LastName").send_keys("Doe")
driver.find_element(By.ID,"Email").send_keys("John@gmail.com")
driver.find_element(By.ID,"Password").send_keys("123456")
driver.find_element(By.ID,"ConfirmPassword").send_keys("123456")
driver.find_element(By.ID,"register-button").click()
driver.close()'''

#Task4
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.ID,"singleFileInput").send_keys(r"C:\Users\hp5cd\Desktop\IT\Bracelet - Copy.jpg")
# driver.find_element(By.ID,"multipleFilesInput").send_keys(r"C:\Users\hp5cd\Desktop\IT\Flower Pot (1).jpg")
# driver.find_element(By.ID,"multipleFilesInput").send_keys(r"C:\Users\hp5cd\Desktop\IT\Bracelet - Copy.jpg")
# driver.find_element(By.ID,"multipleFilesInput").send_keys(r"C:\Users\hp5cd\Desktop\IT\Reusable Cup.jpg")
'''driver.find_element(By.ID, "multipleFilesInput").send_keys(
    "C:\\Users\\hp5cd\\Desktop\\IT\\Flower Pot (1).jpg\n"
    "C:\\Users\\hp5cd\\Desktop\\IT\\Bracelet - Copy.jpg\n"
    "C:\\Users\\hp5cd\\Desktop\\IT\\Reusable Cup.jpg"
)'''
'''list = [r"C:\Users\hp5cd\Desktop\IT\Flower Pot (1).jpg",r"C:\Users\hp5cd\Desktop\IT\Bracelet - Copy.jpg",r"C:\Users\hp5cd\Desktop\IT\Reusable Cup.jpg"]
for i in list:
    driver.find_element(By.ID,"multipleFilesInput").send_keys(i)'''

#driver.close()


