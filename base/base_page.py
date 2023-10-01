from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    """We call the functions to be used in the base class"""
    
    def __init__(self, driver):
        """constructor with initial values"""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        

    def find_element(self, *locator):
        """finds and wait element function"""
        return self.driver.find_element(*locator)
        
        
    def click_element(self, *locator):
        """performs the click function"""
        self.find_element(*locator).click()
        
        
    def send_text(self, text, *locator):
        """performs the sending text function"""
        self.find_element(*locator).send_keys(text)
        
        
    def clear_text(self, *locator):
        """performs the clear text function"""
        self.find_element(*locator).clear()
        

        return self 
    """enables using send function immediately"""

    def wait_element(self, element):
        """allows the page to load and find the element"""
        return self.wait.until(ec.presence_of_all_elements_located(element))
        

    def find_elements(self, index, *element):
        self.driver.find_elements(*element)[index].click()
        """finds and wait elements function"""
