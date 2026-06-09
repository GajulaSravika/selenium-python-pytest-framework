from selenium.webdriver.common.by import By
from selenium import webdriver


class CheckOut_Page:
    def __init__(self,driver):
        self.driver=driver
        self.driver.checkout_button_id = "checkout"
    def checkout(self):
        self.driver.find_element(By.ID, self.driver.checkout_button_id).click()
