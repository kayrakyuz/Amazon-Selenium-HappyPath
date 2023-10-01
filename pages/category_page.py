from selenium.webdriver.common.by import By

from base.base_page import BasePage


class CategoryPage(BasePage):
    """Performs transactions on the Category Page"""

    NEXT_BTN = (By.XPATH, './/a[contains(@class,"s-pagination-next")]')
    CLICK_PRODUCT = (By.CSS_SELECTOR, ".a-size-medium.a-color-base.a-text-normal")

    def __init__(self, driver):
        """constructor with initial values"""
        self.driver = driver
        self.methods = BasePage(self.driver)

    def click_to_next_btn(self):
        """goes to next category page"""
        self.find_element(*self.NEXT_BTN).click()

    def click_to_third_element(self, index):
        """clicks the third element on category page"""
        self.find_elements(index, *self.CLICK_PRODUCT)
