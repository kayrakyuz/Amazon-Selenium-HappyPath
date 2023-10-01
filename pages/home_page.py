import self as self
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class HomePage(BasePage):
    """Performs transactions on the Home Page"""
    LOGIN_BTN = (By.ID, 'nav-link-accountList-nav-line-1')
    SEARCH_TEXT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')

    def __init__(self, driver):
        """constructor with initial values"""
        self.driver = driver
        self.methods = BasePage(self.driver)

    def click_to_login_btn(self):
        """clicks the login button and goes to the login page"""
        self.find_element(*self.LOGIN_BTN).click()

    def search(self, text):
        """clicks the search bar"""
        self.send_text(text, *self.SEARCH_TEXT)

    def search_btn(self):
        """searchs product by clicking search button"""
        self.find_element(*self.SEARCH_BTN).click()
