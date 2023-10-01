import self as self
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):
    """Performs transactions on the Login Page"""
    EMAIL = (By.ID, 'ap_email')
    CONTINUE = (By.ID, 'continue')
    PASSWORD = (By.ID, 'ap_password')
    SUBMIT_BTN = (By.ID, 'signInSubmit')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BasePage(self.driver)

    def click_to_continue_btn(self):
        self.find_element(*self.CONTINUE).click()

    def click_to_submit_btn(self):
        self.find_element(*self.SUBMIT_BTN).click()

    def send_username(self, text):
        self.send_text(text, *self.EMAIL)

    def send_password(self, text):
        self.send_text(text, *self.PASSWORD)



