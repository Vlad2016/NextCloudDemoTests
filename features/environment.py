import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import ConfigReader


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))
    context.driver.find_element(By.XPATH, "//div[@class='login-option']/a").click()


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="failed_screenshot", attachment_type=AttachmentType.PNG)
