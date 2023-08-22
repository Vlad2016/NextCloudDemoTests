from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    app_dashboard_xpath = "//div[@id='app-dashboard']"
    files_app_menu_xpath = "//li[@data-app-id='{txt}']"
    def get_app_dashboard_visibility(self):
        return self.driver.find_element(By.XPATH, self.app_dashboard_xpath).is_displayed()

    def select_app_in_app_menu(self, app_title):
        self.driver.find_element(By.XPATH, self.files_app_menu_xpath.format(txt = app_title)).click()
