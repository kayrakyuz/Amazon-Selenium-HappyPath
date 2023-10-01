from selenium.webdriver.common.by import By

from base.base_page import BasePage


class CartPage(BasePage):
    """Performs transactions on the Card Page"""

    DELETE = (By.CSS_SELECTOR, 'input[name="submit.deleteItem"]')

    def __init__(self, driver):
        """constructor with initial values"""
        self.driver = driver
        self.methods = BasePage(self.driver)

    def delete_btn(self):
        self.find_element(*self.DELETE).click()
        """deletes item"""
