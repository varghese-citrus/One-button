import time

from behave import given, then

from context.driver import driver
from pages.login_page import LoginPage
from context.config import settings


"""Hooks for interacting with google search"""


@given(u'Provide the username <username> and password <password>')
def provide_credentials(context):
    username = settings.username
    password = settings.password
    login_page = LoginPage.get_instance()
    login_page.enter_username(username)
    login_page.click_on_next_button()
    login_page.enter_password(password)


@given("Click on the Login button")
def click_sign_button(context):
    login_page = LoginPage.get_instance()
    login_page.click_on_signin_button()
    login_page.click_on_no_button()


@then("Login is successful and the OneButton dashboard is opened")
def step_impl(context):
    login_page = LoginPage.get_instance()
    page_title = login_page.get_page_title()
    driver.get_driver()
    try:
        assert page_title == "One Button", "Failed to load OneButton dashboard."
    except AssertionError:
        driver.take_screenshot(context.scenario)
        raise
