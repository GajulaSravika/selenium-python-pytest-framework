import pytest
from Pages.login_page import LoginPage
from Pages.ProductsPage import Products_Page
from Pages.checkout import CheckOut_Page
from Pages.address import Address
def test_end_to_end(driver):
    loginpage=LoginPage(driver)
    loginpage.login("standard_user","secret_sauce") 
    products_page=Products_Page(driver)
    products_page.products()
    products_page.click_cart()
    checkout_page=CheckOut_Page(driver)   
    checkout_page.checkout()
    address_page=Address(driver)
    address_page.address_info("John","Doe","12345")
    assert address_page.verify_info()=="wrong information"

