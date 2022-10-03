
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time

from selenium.webdriver.common.by import By

def test_runtimefetch():
    path="C:\\MyFramework\\Drivers\\\ChromeDriver5\\chromedriver.exe"
    driver = Chrome(executable_path=path)

    driver.get("http://theTestingworld.com/testings")
    driver.maximize_window()

    obj=Select(driver.find_element("name","sex"))
    obj.select_by_visible_text("Female")

    #to fetch all available optn
    for op in obj.options:
        print(op.text)

    #fetch selected option
    print("selected gender is:"+obj.first_selected_option.text)


