from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


class TestCheckAmazon():
    """The section where we make the settings and create the objects"""
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = "https://www.amazon.com/"
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    category_page = CategoryPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    def navigate_to_home_page(self):
        """driver settings made and website published"""

        self.driver.maximize_window()
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 15)


if __name__ == '__main__':
    TestCheckAmazon()
