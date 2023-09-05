from behave import *

from features.pages.LoginPage import LoginPage
from utilities import ConfigReader


@given('Open Login page')
def step_impl(context):
    LoginPage(context.driver)


@when('Login as "{username}"')
def step_impl(context, username):
    login_page = LoginPage(context.driver)
    login_page.type_user_into_input(ConfigReader.read_configuration("basic info", username))
    login_page.type_password_into_input()
    login_page.click_login_button()
