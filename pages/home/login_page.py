from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
from pages.home.forget_password_page import ForgetPasswordPage
import logging


class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _login_link = "//a[@href='/login']"
    _email_field = "//input[@id='login_field']"
    _password_field = "//input[@id='password']"
    _sign_in_btn = "//input[@name='commit']"
    _login_page_text = "//h1[contains(text(),'Sign in to GitHub')]"
    _login_failed_msg = "//div[@class='container-lg px-2']//button[@class='flash-close js-flash-close']"
    _forget_password = "//input[@id='email_field']"
    _signup_link = "//a[@href='/join?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home']"
    _signup_page_text = "//h1[contains(text(),'Create your account')]"

    def click_on_forget_password_link(self):
        """
        Click on forget password link
        :return:
        """
        try:

            self.elementClick(locator=self._forget_password, locator_type="id")
            return ForgetPasswordPage(self.driver)
        except Exception as e:
            raise Exception("Unable to click on forget password link")

    def click_on_signup_link(self):
        """
        Click on signup link
        :return:
        """
        try:
            self.elementClick(locator=self._signup_link, locator_type="xpath")
        except Exception as e:
            raise Exception("Unable to click on signup link " + str(e))



    def click_login_link(self):
        """
        Click on Login Link
        :return:
        """
        try:
            self.elementClick(locator=self._login_link, locator_type="xpath")
        except Exception as e:
            raise Exception("Unable to click on login link " + str(e))

    def enter_email(self, email):
        """
        Enter email at email text field
        :param email:
        :return:
        """
        try:
            self.sendKeys(data=email, locator=self._email_field, locator_type="xpath")
        except Exception as e:
            raise Exception("Unable to send data to email field " + str(e))

    def enter_password(self, password):
        """
        Enter Password at password text field
        :param password:
        :return:
        """
        try:
            self.sendKeys(data=password, locator=self._password_field, locator_type="xpath")
        except Exception as e:
            raise Exception(" Unable to send data to password field " + str(e))

    def click_sign_in_btn(self):
        """
        Click on sign in button
        :return:
        """
        try:
            self.elementClick(locator=self._sign_in_btn, locator_type="xpath")
        except Exception as e:
            raise Exception("Unable to click on sign in button " + str(e))

    def login(self, email= "", password= ""):
        """
        Login to git
        :param email:
        :param password:
        :return:
        """
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in_btn()

    def verify_login_page_displayed(self):
        try:
            self.click_login_link()
            is_element_present = self.isElementPresent(locator=self._login_page_text, locator_type="xpath")
            return is_element_present
        except Exception as e:
            raise Exception("Unable to find login page text element on the page " + str(e))

    def verify_signup_page_displayed(self):
        try:
            self.click_on_signup_link()
            is_element_present = self.isElementPresent(locator=self._signup_link, locator_type="xpath")
            return is_element_present
        except Exception as e:
            raise Exception("Unable to find signup page text element on the page " + str(e))

    def verify_login_failed_(self):
        try:
            result = self.isElementPresent(locator=self._login_failed_msg, locator_type="xpath")
            return result
        except Exception as e:
            raise Exception("Unable to find login failed text on the page " + str(e))



