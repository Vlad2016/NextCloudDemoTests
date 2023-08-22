from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import ConfigReader


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    login_options_label_xpath = "//h1[text()='Login options:']"
    direct_login_button_xpath = "//a[text()='Direct log in']"
    account_name_or_email_input_xpath = "//input[@id='user']"
    password_input_xpath = "//input[@id='password']"
    log_in_button_xpath = "//button[@type='submit']"

    def click_direct_login(self):
        self.driver.find_element(By.XPATH, self.direct_login_button_xpath).click()

    def get_login_options_label_visibility(self):
        return self.driver.find_element(By.XPATH, self.login_options_label_xpath).is_displayed()

    def type_user_into_input(self, user):
        self.driver.find_element(By.XPATH, self.account_name_or_email_input_xpath).send_keys(user)

    def type_password_into_input(self):
        password = ConfigReader.read_configuration("basic info", "admin_password")
        self.driver.find_element(By.XPATH, self.password_input_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.log_in_button_xpath).click()
