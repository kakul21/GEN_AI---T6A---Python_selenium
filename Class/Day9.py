from operator import index
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
o.add_experimental_option('prefs',{'safebrowsing.enabled':True})
o.add_argument('--disable-notifications')
driver = Chrome(options=o)

# iframe - one web page embedded in another web page
# We can switch to iframe by
# - using index
# - using name
# - using locator

# - using index - driver.switch_to.frame(0)

'''driver.get("http://localhost:5500/Page1.html")
driver.maximize_window()
driver.find_element(By.ID,"input 1").send_keys("First input")
driver.switch_to.frame(0)
driver.find_element(By.ID,"input 2").send_keys("Second input")
driver.switch_to.frame(0)
driver.find_element(By.ID,"input 3").send_keys("Third input")
driver.close()'''

# - using name - driver.switch_to.frame('h2')

'''driver.get("http://localhost:5500/Page1.html")
driver.maximize_window()
driver.find_element(By.ID,"input 1").send_keys("First input")
driver.switch_to.frame("first")
driver.find_element(By.ID,"input 2").send_keys("Second input")
driver.switch_to.frame("second")
driver.find_element(By.ID,"input 3").send_keys("Third input")
driver.close()'''

# - using ID - driver.switch_to.frame('ID')
# - sometimes it works sometimes not
'''driver.get("http://localhost:5500/Page1.html")
driver.maximize_window()
driver.switch_to.frame("frame1")
driver.find_element(By.ID,"input 2").send_keys("Second input")
driver.close()'''

# - using web element
'''driver.get("http://localhost:5500/Page1.html")
driver.maximize_window()
driver.find_element(By.ID,"input 1").send_keys("First input")
web_element = driver.find_element(By.XPATH,"//iframe[@src='Page2.html']")
driver.switch_to.frame(web_element)
driver.find_element(By.ID,"input 2").send_keys("Second input")
web_element2 = driver.find_element(By.XPATH,"//iframe[@src='Page3.html']")
driver.switch_to.frame(web_element2)
driver.find_element(By.ID,"input 3").send_keys("Third input")
driver.close()'''

'''driver.get("http://localhost:5500/Page1.html")
driver.maximize_window()
inp1=driver.find_element(By.ID,"input 1")
inp1.send_keys("First input")
driver.switch_to.frame(0)
inp2 = driver.find_element(By.ID,"input 2")
inp2.send_keys("Second input")
driver.switch_to.parent_frame()
inp1.clear()
driver.switch_to.frame(0)
driver.switch_to.frame(0)
inp3=driver.find_element(By.ID,"input 3")
inp3.send_keys("Third input")
# driver.switch_to.parent_frame()
# inp2.clear()
driver.switch_to.default_content()
driver.close()'''

# Alerts and Pop-ups

# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()

## Simple alert
'''driver.find_element(By.ID,"alertBtn").click()
alert = driver.switch_to.alert
sleep(3)
alert.accept()'''

## Confirmation_alert
'''driver.find_element(By.ID,"confirmBtn").click()
alert = driver.switch_to.alert
sleep(3)
# alert.accept()
alert.dismiss()'''

## Prompt alert
'''driver.find_element(By.ID,"promptBtn").click()
alert = driver.switch_to.alert
sleep(3)
alert.send_keys("Kakul")
sleep(3)
alert.accept()'''

## Download and upload
'''driver.get("https://demoqa.com/upload-download")
driver.maximize_window()
# download = driver.find_element(By.ID,"downloadButton")
# download.click()
upload = driver.find_element(By.ID,"uploadFile")
upload.send_keys(r"C:\\Users\\hp5cd\\Desktop\\IT\\Bracelet.jpg")
# driver.close()'''

## Safe Browsing by adding o.add_experimental_option('prefs',{'safebrowsing.enabled':True})

'''driver.get("https://www.python.org/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/downloads/']"))).click()
# driver.find_element(By.XPATH,"//a[@href='/downloads/']").click()
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//a[text()='Download Python install manager']")
)).click()'''

## Disable Notifications
# driver.get("https://www.easemytrip.com/flights.html?utm_campaign=788997081&utm_source=g_c&utm_medium=cpc&utm_term=e_easemytrip&adgroupid=39319940377&gad_source=1&gad_campaignid=788997081&gbraid=0AAAAADo_0-h3QJ-p11y-Kv-NZh2sT2JIk&gclid=EAIaIQobChMIiL_5l6O4kwMVgdEWBR1NCjfbEAAYASAAEgL-TfD_BwE")
# driver.maximize_window()

# driver.get("https://www.crocs.in/?srsltid=AfmBOorlPbEj-QfVQT4KyGJpaGo9Y57KmJIdCCRz5Hef8hEwDZaiQx6t")
# driver.maximize_window()

'''driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").click()
sleep(2)
date=driver.find_element(By.CLASS_NAME,"ui-state-default.ng-tns-c69-9.ui-state-active.ng-star-inserted")
date.click()'''

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.find_element(By.ID,"dateOfBirthInput").click()
driver.find_element(By.CLASS_NAME,"react-datepicker__day.react-datepicker__day--026").click()
