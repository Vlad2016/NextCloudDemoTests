from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    app_dashboard_xpath = "//div[@id='app-dashboard']"
    files_app_menu_xpath = "//li[@data-app-id='{txt}']"
    widget_xpath = "//div[@class='panels']/div[@class='panel']"
    customize_button_xpath = "//button[.//span[text()='Customize']]"
    modal_container_xpath = "//div[@class='modal-container']"
    edit_widgets_modal_container_close_button_xpath = modal_container_xpath + "//button[@aria-label='Close modal']"
    widget_by_class_xpath = modal_container_xpath + "//li[@class='panel-{txt}']"
    widget_status_xpath = "//li[@id='status-{txt}']"

    def get_app_dashboard_visibility(self):
        return self.driver.find_element(By.XPATH, self.app_dashboard_xpath).is_displayed()

    def select_app_in_app_menu(self, app_title):
        self.driver.find_element(By.XPATH, self.files_app_menu_xpath.format(txt=app_title)).click()

    def get_widgets_amount(self):
        return len(self.driver.find_elements(By.XPATH, self.widget_xpath))

    def click_customize_button(self):
        self.driver.find_element(By.XPATH, self.customize_button_xpath).click()

    def get_edit_widgets_modal_visibility(self):
        self.driver.implicitly_wait(3)
        return self.driver.find_element(By.XPATH, self.modal_container_xpath).is_displayed()

    def close_edit_widgets_modal(self):
        self.driver.find_element(By.XPATH, self.edit_widgets_modal_container_close_button_xpath).click()

    def select_widget(self, widget):
        self.driver.find_element(By.XPATH, self.widget_by_class_xpath.format(txt=widget)).click()

    def get_widget_visibility(self, widget):
        result = "NOT_VISIBLE"
        if self.driver.find_element(By.XPATH, self.widget_status_xpath.format(txt=widget)).is_displayed():
            result = "VISIBLE"
        return result
