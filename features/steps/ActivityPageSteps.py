from behave import *

from features.pages.ActivityPage import ActivityPage


@then('Verify "{message}" message is "{expected}" on the Activity page')
def step_impl(context, message, expected):
    result = "NOT_VISIBLE"
    if message == ActivityPage(context.driver).get_first_message():
        result = "VISIBLE"
    assert result == expected


@when('Open menu for "{board_title}" board on the Activity page')
def step_impl(context, board_title):
    ActivityPage(context.driver).open_board_menu_by_title(board_title)


@when('Select "{option}" option from menu on the Activity page')
def step_impl(context, option):
    ActivityPage(context.driver).select_option(option)
    ActivityPage(context.driver).confirm_delete_board()
