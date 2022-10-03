from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec

@pytest.fixture()
def enviroment_setup():
    global driver
    path = "C:\\MyFramework\\Drivers\\ChromeDriver5\\chromedriver.exe"
    driver = Chrome(executable_path=path)

    driver.get("http://theTestingworld.com/testings")
    driver.refresh()
    driver.maximize_window()

    yield
    driver.close()

def test_verify_registration(enviroment_setup):


    # work on all dropdown

    obj=Select(driver.find_element("name","sex"))
    obj.select_by_visible_text("Male")

    #wait time

    obj = Select(driver.find_element(By.ID, 'countryId'))
    obj.select_by_visible_text("India")

    wait=WebDriverWait(driver,1000)
    #wait.until(ec.text_to_be_present_in_element(By.ID,'stateId'),"Odisha")

    wait.until(ec.text_to_be_present_in_element((By.ID, 'stateId'), "Odisha"))
    obj = Select(driver.find_element(By.ID, "stateId"))
    obj.select_by_visible_text("Odisha")

    wait.until(ec.text_to_be_present_in_element((By.ID, 'cityId'), "Sambalpur"))
    obj = Select(driver.find_element(By.ID, "cityId"))
    obj.select_by_visible_text("Sambalpur")
    time.sleep(5)



