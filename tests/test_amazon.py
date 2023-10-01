import time
import unittest

from selenium.webdriver.common.by import By
from tests.test_check_amazon import TestCheckAmazon


class TestAmazon(unittest.TestCase, TestCheckAmazon):
    """TEST CASE
            1.  http://www.amazon.com sitesine gidecek ve anasayfanın açıldığını assertion ile onaylayacak,
            2. Login ekranını açıp, bir kullanıcı ile login olunacak ( daha önce siteye üyeliği varsa o olabilir )
            3. Ekranin ustundeki Search alanına 'samsung' yazıp ara butonuna tıklanacak,
            4. Gelen sayfada samsung icin sonuc bulunduğunu onaylayacak,
            5. Arama sonuçlarından 2. sayfaya tıklayacak ve açılan sayfada 2. sayfanin şu an gösterimde oldugunu onaylayacak,
            6. Üstten 3. urunun içindeki 'Add to List' butonuna tıklayacak,
            7. Ekranin en üstündeki 'List' linkine tiklayacak içerisinden Wish listi seçecek,
            8. Acilan sayfada bir onceki sayfada izlemeye alinmis urunun bulundugunu onaylayacak,
            9. Favorilere alinan bu urunun yanindaki 'Delete' butonuna basarak, favorilerimden cikaracak,
            10. Sayfada bu urunun artik favorilere alinmadigini onaylayacak.
        """
    def setUp(self):
        TestCheckAmazon.__init__(self)

    def test_amazon(self):
        """
        performs test for amazon website from homepage to cart page by verifying steps.
        """

        self.navigate_to_home_page()
        self.home_page.click_to_login_btn()
        self.login_page.send_username("kayrakyuz@gmail.com")
        self.login_page.click_to_continue_btn()
        self.login_page.send_password('Kayrar1903')
        self.login_page.click_to_submit_btn()
        time.sleep(2)
        self.home_page.search('samsung')
        self.home_page.search_btn()
        self.assertEqual('"samsung"', self.driver.find_element(By.CSS_SELECTOR, '.a-color-state.a-text-bold').text)
        self.category_page.click_to_next_btn()
        time.sleep(2)
        self.assertFalse(self.driver.find_element(By.CSS_SELECTOR, '.s-pagination-item.s-pagination-selected').is_selected())
        self.category_page.click_to_third_element(2)
        product_title = self.driver.find_element(By.CSS_SELECTOR, '#productTitle').text

        self.product_page.add_to_wishlist()
        self.product_page.go_to_wishlist()
        wishlist_product_title = self.driver.find_element(By.CSS_SELECTOR, 'h2 a').text
        self.assertEqual(product_title, wishlist_product_title , "Text is not equals!")
        self.cart_page.delete_btn()
        delete_info = self.driver.find_element(By.XPATH, ".//*[text()='Deleted']").text
        self.assertEqual(delete_info, "Deleted", "Product is not deleted")

    def tear_down(self):
        """closes driver"""
        self.driver.quit()


