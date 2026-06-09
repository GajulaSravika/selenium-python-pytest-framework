from selenium.webdriver.common.by import By
from selenium import webdriver

class Products_Page:
    def __init__(self,driver):
        self.driver=driver
        self.driver.product_add_to_cart_id = "add-to-cart-sauce-labs-backpack"
        self.driver.cart_class_name = "shopping_cart_link"
    def products(self):
        self.driver.find_element(By.ID, self.driver.product_add_to_cart_id).click()
    def click_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.driver.cart_class_name).click()