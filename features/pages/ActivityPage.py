from selenium.webdriver.common.by import By


class ActivityPage:

    def __init__(self, driver):
        self.driver = driver

    last_activity_message_xpath = "//div[@class='messagecontainer']/div[@class='activitysubject']"
    board_menu_by_title_xpath = "//div[@class='app-navigation-entry'][.//a[@title='{title}']]/div"
    board_menu_option_xpath = "//div[@class='open']//li[.//span[text()='{option}']]"
    delete_button_on_dialog_xpath = "//div[@class='oc-dialog']//button[text()='Delete']"

    def get_first_message(self):
        return self.driver.find_element(By.XPATH, self.last_activity_message_xpath).text

    def open_board_menu_by_title(self, board_title):
        self.driver.find_element(By.XPATH, self.board_menu_by_title_xpath.format(title=board_title)).click()

    def select_option(self, option):
        self.driver.find_element(By.XPATH, self.board_menu_option_xpath.format(option=option)).click()

    def confirm_delete_board(self):
        self.driver.find_element(By.XPATH, self.delete_button_on_dialog_xpath).click()
