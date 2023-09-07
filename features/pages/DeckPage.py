from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class DeckPage:

    def __init__(self, driver):
        self.driver = driver

    add_board_button_xpath = "//li[.//span[contains(text(), 'Add board')]]"
    new_board_name_input_xpath = "//input[@placeholder='Board name']"

    def click_add_board_button(self):
        self.driver.find_element(By.XPATH, self.add_board_button_xpath).click()

    def type_new_board_name(self, board_name):
        self.driver.find_element(By.XPATH, self.new_board_name_input_xpath).send_keys(board_name)
        self.driver.find_element(By.XPATH, self.new_board_name_input_xpath).send_keys(Keys.RETURN)