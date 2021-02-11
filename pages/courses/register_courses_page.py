import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

#######################################
###########Locators####################
#######################################

    _search_box = "course"  #name
    _search_icon = "//i[@class= 'fa fa-search']"
    _course = "//h4[contains(@class, 'dynamic-heading') and contains(text(),'{0}')]" #xpath
    _all_courses = "//a[(@href='/courses') and contains(text(),'ALL COURSES')]" #class
    _enroll_button = "//button[contains(text(),'Enroll in Course')]" #xpath
    _cc_num = "//input[@placeholder = 'Card Number']" #xpath
    _cc_exp = "exp-date" #name
    _cc_cvv = "//input[@placeholder ='Security Code']"
    _submit_enroll = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"
    _enroll_error_message = "//span[contains(text(),'Your card number is invalid')]"

    def enterCourseName(self,name):
        self.sendKeys(name, locator= self._search_box, locatorType= 'name')
        self.elementClick(locator= self._search_icon, locatorType="xpath")

    def selectCourseToEnroll(self, fullcoursename):
        self.elementClick(locator= self._course.format(fullcoursename), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button,locatorType="xpath")

    def enterCardNum(self, num):
        time.sleep(8)
        #self.switchToFrame(name="__privateStripeFrame6675")
        self.SwitchFrameByIndex(self._cc_num, locatorType= "xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType= "xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        #self.switchToFrame(name="__privateStripeFrame6677")
        self.SwitchFrameByIndex(self._cc_exp, locatorType= "name")
        self.sendKeys(exp, locator = self._cc_exp, locatorType= "name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        #self.switchToFrame(name="__privateStripeFrame6676")
        self.SwitchFrameByIndex(self._cc_cvv, locatorType= "xpath")
        self.sendKeys(cvv, locator = self._cc_cvv, locatorType= "xpath")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self,num,exp,cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self,num='',exp ='',cvv=''):
        self.clickOnEnrollButton()
        self.webScroll("down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message,"xpath")
        result = self.isElementDisplayed(locator= self._enroll_error_message, locatorType= "xpath", element = messageElement)
        return result

    def searchAnotherCourse(self):
        self.webScroll("up")
        self.elementClick(locator= self._all_courses, locatorType= "xpath")
