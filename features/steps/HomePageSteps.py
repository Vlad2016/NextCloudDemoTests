from behave import *

from features.pages.HomePage import HomePage


@then('Verify user is logged in on the Home page')
def step_impl(context):
    home_page = HomePage(context.driver)
    assert home_page.get_app_dashboard_visibility()


@when('Click "{app_title}" in app menu on the Home page')
def step_impl(context, app_title):
    HomePage(context.driver).select_app_in_app_menu(app_title)