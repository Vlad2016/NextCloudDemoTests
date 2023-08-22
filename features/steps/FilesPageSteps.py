from behave import *

from features.pages.FilesPage import FilesPage


@when('Select "{foldername}" folder on the Files page')
def step_impl(context, foldername):
    FilesPage(context.driver).click_on_folder_by_title(foldername)


@when('Select "{filename}" file on the Files page')
def step_impl(context, filename):
    FilesPage(context.driver).click_on_file_by_title(filename)


@then('Verify office document is opened on the Files page')
def step_impl(context):
    assert FilesPage(context.driver).get_opened_office_file_visibility()