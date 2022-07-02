
from selenium import webdriver
import time
import unittest
from selenium.webdriver.chrome.service import Service
from pages.loginpage import LoginPage



class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service('../Driver/chromedriver')
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://www.saucedemo.com/")

    def test_Valid_Login(self):
        driver = self.driver
        time.sleep(2)
        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login_button()
        time.sleep(3)
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        driver.close()

    def test_Invalid_Username(self):
        driver = self.driver
        time.sleep(2)
        login = LoginPage(driver)
        login.enter_username("israr-testing")
        login.enter_password("secret_sauce")
        login.click_login_button()
        assert driver.current_url ==  "https://www.saucedemo.com/"

    def test_Invalid_Password(self):
        driver = self.driver
        time.sleep(2)
        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("1234")
        login.click_login_button()
        assert driver.current_url ==  "https://www.saucedemo.com/"

    def test_Invalid_Login(self):
        driver = self.driver
        time.sleep(2)
        login = LoginPage(driver)
        login.enter_username("testing")
        login.enter_password("1234")
        login.click_login_button()
        assert driver.current_url ==  "https://www.saucedemo.com/"



