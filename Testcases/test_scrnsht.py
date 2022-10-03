from selenium.webdriver import Chrome

def test_scrnsht():
    path="C:\\MyFramework\\Drivers\\ChromeDriver5\\chromedriver.exe"
    driver = Chrome(executable_path=path)

    driver.get("http://theTestingworld.com/testings")
    driver.maximize_window()
    #go to Login bar
    driver.find_element("xpath","//label[text()='Login']").click()
    driver.find_element("name","_txtUserName").send_keys("test")
    driver.find_element("name","_txtPassword").send_keys("test")
    driver.find_element("xpath","//input[@type='Submit' and @value='Login']").click()


    driver.get_screenshot_as_file("C:/Users/namra/PycharmProjects/seleniumAutomation/TestingWorld.png")
