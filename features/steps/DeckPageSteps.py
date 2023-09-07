from behave import *

from features.pages.DeckPage import DeckPage


@when('Create a new "{board_name}" board on the Deck page')
def step_impl(context, board_name):
    DeckPage(context.driver).click_add_board_button()
    DeckPage(context.driver).type_new_board_name(board_name)
