#open browser
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By

def test_firsttestcase():
    path="C:\\MyFramework\\Drivers\\\ChromeDriver5\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://theTestingworld.com/testings")
    driver.maximize_window()
    #driver.implicitly_wait(200)
    #Enter data into the Textboxes
    driver.find_element("name","fld_username").send_keys("Ankita")
    driver.find_element("xpath","//input[@name='fld_email']").send_keys("testingworld@gmail.com")

    driver.find_element("name","fld_password").send_keys("abcd123")
    driver.find_element("name","fld_cpassword").send_keys("abcd123")
    driver.find_element("xpath","//input[@value='home']").click()
    driver.find_element("name","terms").click()

    #work on dropdown
    obj=Select(driver.find_element(By.NAME,value="sex"))
    #obj.select_by_visible_text("Male")
    obj.select_by_index(2)#position

    #working on radiobutton
    driver.find_element("xpath", "//input[@value='office']").click()
    #working on checkbox
    driver.find_element("name","terms").click()
    #work on button
    driver.find_element("xpath","//input[@type='submit']").click()
    #work on links
    #driver.find_element(By.LINK_TEXT,value='Read Detail').click()


    time.sleep(5)
    driver.close()
    driver.quit()
