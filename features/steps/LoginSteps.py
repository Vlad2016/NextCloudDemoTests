from behave import *

from features.pages.LoginPage import LoginPage
from utilities import ConfigReader


# login_page = LoginPage()


@given('Open Login page')
def step_impl(context):
    login_page = LoginPage(context.driver)
    # assert login_page.get_login_options_label_visibility()

@when('Login as "{username}"')
def step_impl(context, username):
    login_page = LoginPage(context.driver)
    # login_page.click_direct_login()
    login_page.type_user_into_input(ConfigReader.read_configuration("basic info", username))
    login_page.type_password_into_input()
    login_page.click_login_button()


