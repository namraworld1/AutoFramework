#keyboard operation
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_actionclass():
    path="C:\\MyFramework\\Drivers\\\ChromeDriver5\\chromedriver.exe"

    driver = Chrome(executable_path=path)
    driver.get("http://theTestingworld.com/testings")
    driver.find_element("name","fld_username").send_keys("Hello")

    act=ActionChains(driver)
    act.send_keys(Keys.TAB).perform()
    act.key_down(Keys.CONTROL).send_keys('a').perform()
    #act.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys (Keys.DELETE).perform()

