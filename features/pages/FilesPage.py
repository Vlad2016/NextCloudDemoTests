from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class FilesPage:

    def __init__(self, driver):
        self.driver = driver

    files_container_xpath = "//div[@id='app-content-files']"
    folder_row_in_files_container_by_text_xpath = files_container_xpath + "//td[.//span[@title='Documents']]"
    file_row_in_files_container_by_text_xpath = files_container_xpath + "//td[.//span[@title='Welcome to Nextcloud Hub']]"
    office_file_frame_xpath = "//iframe[@id='onlyofficeFrame']"

    def click_on_folder_by_title(self, title):
        self.driver.find_element(By.XPATH, self.folder_row_in_files_container_by_text_xpath).click()

    def click_on_file_by_title(self, title):
        self.driver.find_element(By.XPATH, self.file_row_in_files_container_by_text_xpath).click()
        # ec = expected_conditions.visibility_of_element_located(file)
        # WebDriverWait(self.driver, 10).until(ec)
        # file.click()

    def get_opened_office_file_visibility(self):
        return self.driver.find_element(By.XPATH, self.office_file_frame_xpath).is_displayed()
