from behave import *

from features.pages.PhotosPage import PhotosPage


@then('Verify App Navigation list is "{expected}" on the Photos page')
def step_impl(context, expected):
    photos_page = PhotosPage(context.driver)
    assert photos_page.get_app_navi_list_visibility() == expected


@when('Select "{item}" item in App Navigation menu on the Photos page')
def step_impl(context, item):
    PhotosPage(context.driver).select_item_in_app_navi_list(item)


@when('Select "{filename}" image on the Photos page')
def step_impl(context, filename):
    PhotosPage(context.driver).select_image_by_filename(filename)


@when('Select "{filename}" video on the Photos page')
def step_impl(context, filename):
    PhotosPage(context.driver).select_video_by_filename(filename)


@then('Verify modal-container is opened on the Photos page')
def step_impl(context):
    photo_page = PhotosPage(context.driver)
    assert photo_page.get_modal_container_visibility()


@when('Close modal-container on the Photos page')
def step_impl(context):
    PhotosPage(context.driver).close_modal_container()
