from behave import *

from features.pages.HomePage import HomePage


@then('Verify user is logged in on the Home page')
def step_impl(context):
    home_page = HomePage(context.driver)
    assert home_page.get_app_dashboard_visibility()


@when('Click "{app_title}" in app menu on the Home page')
def step_impl(context, app_title):
    HomePage(context.driver).select_app_in_app_menu(app_title)


@then('Verify no widgets are present on the Home page')
def step_impl(context):
    home_page = HomePage(context.driver)
    assert home_page.get_widgets_amount() == 0


@when('Click "Customize" button on the Home page')
def step_impl(context):
    HomePage(context.driver).click_customize_button()


@then('Verify \'Edit widgets\' modal-container is opened on the Home page')
def step_impl(context):
    home_page = HomePage(context.driver)
    assert home_page.get_edit_widgets_modal_visibility()


@when(u'Close modal-container on the Home page')
def step_impl(context):
    HomePage(context.driver).close_edit_widgets_modal()


@when('Select "{widget}" widget in modal-container on the Home page')
def step_impl(context, widget):
    HomePage(context.driver).select_widget(widget.lower())


@then('Verify "{widget}" widget is "{expected}" on the Home page')
def step_impl(context, widget, expected):
    home_page = HomePage(context.driver)
    assert home_page.get_widget_visibility(widget.lower()) == expected
