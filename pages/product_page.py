from selenium.webdriver.common.by import By

from base.base_page import BasePage


class ProductPage(BasePage):
    """Performs transactions on the Product Page"""
    ADD_WISHLIST = (By.CSS_SELECTOR, '#add-to-wishlist-button-submit')
    GO_WISHLIST = (By.CSS_SELECTOR, '#huc-view-your-list-button')

    def __init__(self, driver):
        """constructor with initial values"""
        self.driver = driver
        self.methods = BasePage(self.driver)

    def add_to_wishlist(self):
        """adds product to a wishlist"""
        self.find_element(*self.ADD_WISHLIST).click()

    def go_to_wishlist(self):
        """goes to wishlist"""
        self.find_element(*self.GO_WISHLIST).click()
