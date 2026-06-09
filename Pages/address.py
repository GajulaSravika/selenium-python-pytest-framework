from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Address:
    def __init__(self,driver):
        self.driver=driver
        self.first_name_textbox_id = "first-name"
        self.last_name_textbox_id = "last-name" 
        self.postal_code_textbox_id = "postal-code"
        self.continue_button_id = "continue"
        self.finish_button_id = "finish"
    def address_info(self,first_name,last_name,postal_code):
        self.driver.find_element(By.ID, self.first_name_textbox_id).send_keys(first_name)
        self.driver.find_element(By.ID, self.last_name_textbox_id).send_keys(last_name)
        self.driver.find_element(By.ID, self.postal_code_textbox_id).send_keys(postal_code)
        self.driver.find_element(By.ID, self.continue_button_id).click()
        print(self.driver.current_url)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, self.finish_button_id)))
        self.driver.find_element(By.ID, self.finish_button_id).click()
    def verify_info(self):
        info=self.driver.find_element(By.CLASS_NAME, "complete-header").text
        return info