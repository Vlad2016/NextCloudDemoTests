from selenium.webdriver.common.by import By


class PhotosPage:

    def __init__(self, driver):
        self.driver = driver

    app_navi_list_xpath = "//ul[@class='app-navigation__list']"
    app_navi_item_xpath = app_navi_list_xpath + "//li[.//span[contains(text(), '{text}')]]"
    image_by_filename_xpath = "//li[.//img[@alt='{image}']]"
    video_by_filename_xpath = "//li[.//a[contains(@aria-label, '{video}')]]"
    modal_container_xpath = "//div[@class='modal-container']"
    modal_container_close_button_xpath = "//div[@class='modal-header']//button[@aria-label='Close modal']"
    def get_app_navi_list_visibility(self):
        result = "NOT_VISIBLE"
        if self.driver.find_element(By.XPATH, self.app_navi_list_xpath).is_displayed():
            result = "VISIBLE"
        return result

    def select_item_in_app_navi_list(self, item):
        self.driver.find_element(By.XPATH, self.app_navi_item_xpath.format(text=item)).click()

    def select_image_by_filename(self, filename):
        self.driver.find_element(By.XPATH, self.image_by_filename_xpath.format(image=filename)).click()

    def get_modal_container_visibility(self):
        return self.driver.find_element(By.XPATH, self.modal_container_xpath).is_displayed()

    def close_modal_container(self):
        self.driver.find_element(By.XPATH, self.modal_container_close_button_xpath).click()


    def select_video_by_filename(self, filename):
        self.driver.find_element(By.XPATH, self.video_by_filename_xpath.format(video=filename)).click()
