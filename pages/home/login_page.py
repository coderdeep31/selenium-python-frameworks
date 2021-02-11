from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class Loginpage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _login_link = 'SIGN IN'
    _email_field = 'email'
    _password_field = 'password'
    _login_button = "//input[@type='submit']"

    def clickLoginLink(self):
        self.elementClick(self._login_link,"link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button,'xpath')

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(".zl-navbar-rhs-img", locatorType='css')
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(".//span[contains(text(),'Your username or password is invalid. Please try again.')]","xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Google")
