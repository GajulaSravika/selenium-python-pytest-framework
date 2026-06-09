from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_id = "user-name"
        self.password_textbox_id = "password"
        self.login_button_id = "login-button"
    def login(self,username,password):
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)
        self.driver.find_element(By.ID, self.login_button_id).click()
        assert "inventory" in self.driver.current_url