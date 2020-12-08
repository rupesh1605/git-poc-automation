from selenium import webdriver
from pages.home.login_page import LoginPage
from pages.home.forget_password_page import ForgetPasswordPage
from utilities.test_status import TestStatus
from utilities.constants import Constants
import utilities.custom_logger as cl
import unittest
import pytest, logging


@pytest.mark.usefixtures("oneTimeSetUp", "SetUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=1)
    def test_git_login_page_displayed(self):
        """
        Verify Lofin page is displayed
        :return:
        """
        is_login_page_dispayed = self.lp.verify_login_page_displayed()
        self.ts.markFinal("test_git_login_page_displayed", is_login_page_dispayed, "Verify login page is displayed")

    @pytest.mark.run(order=2)
    def test_email_field_is_mandatory(self):
        """
        Verify Email field is mandatory
        :return:
        """
        self.lp.login(password=Constants.PASSWORD)
        is_login_failed = self.lp.verify_login_failed_()
        self.ts.markFinal("test_email_field_is_mandatory", is_login_failed, "Verify email field is mandatory")

    @pytest.mark.run(order=3)
    def test_password_field_is_mandatory(self):
        """
        Verify Password field is mandatory
        :return:
        """
        self.lp.login(email=Constants.EMAIL)
        is_login_failed = self.lp.verify_login_failed_()
        self.ts.markFinal("test_password_field_is_mandatory", is_login_failed, "Verify password field is mandatory")

    @pytest.mark.run(order=4)
    def test_forget_password_ink(self):
        """
        Verify Forget password link
        :return:
        """
        is_login_page_displayed = self.lp.verify_login_page_displayed()
        self.ts.mark(is_login_page_displayed, "Verify login page is displayed")
        forget_password_obj = self.click_on_forget_password_link()
        forget_password_obj.enter_email_at_forget_password_text_field(email=Constants.WRONG_EMAIL)
        forget_password_obj.click_on_send_password_reset_btn()
        error_text = forget_password_obj.get_error_text()
        if error_text.__contains__(Constants.ERROR_MSG):
            self.log.info("Error message is displayed successfully")
        else:
            self.ts.mark(False, "Verify error message ")
        self.log.info("Verify first letter of error is 'That'")
        error_text_list = error_text.split(" ")
        if str(error_text_list[0]) == str("That"):
            self.log.info("First word of error message is 'That' ")
        else:
            self.ts.markFinal("test_forget_password_ink", False, "Verify first word of error text ")

    @pytest.mark.run(order=5)
    def test_verify_signup_page_is_displayed(self):
        """
        Verify sign up page is displayed
        :return:
        """
        is_sign_page_dispayed = self.lp.verify_signup_page_displayed()
        self.ts.markFinal("test_git_login_page_displayed", is_sign_page_dispayed, "Verify login page is displayed")





