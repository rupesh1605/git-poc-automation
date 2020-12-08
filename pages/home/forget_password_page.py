from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class ForgetPasswordPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _email_field = "//input[@id='login_field']"
    _send_password_reset_btn = "//input[@name='commit']"
    _invalid_email_error_msg = "//div[@class='container-lg px-2']"

    def enter_email_at_forget_password_text_field(self, email=""):
        """
        enter email at forget password text field
        :return:
        """
        try:
            self.sendKeys(data=email, locator=self._email_field, locator_type="xpath")
        except Exception as e:
            raise Exception("Unable to send data to email field " + str(e))

    def click_on_send_password_reset_btn(self):
        """
        Click on reset button
        :return:
        """
        try:
            self.elementClick(locator=self._send_password_reset_btn, locator_type="xpath")
        except Exception as e:
            raise Exception("Unable to click on login link " + str(e))

    def get_error_text(self):
        """
        Get the error text
        :return:
        """
        try:
            error_text = self.get_text(locator=self._invalid_email_error_msg, locator_type="xpath")
            return error_text
        except Exception as e:
            raise Exception("Unable to find error text on the page " + str(e))
