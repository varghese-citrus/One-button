import datetime
import time

from behave import given, when, then
from selenium.webdriver import ActionChains

from context.driver import driver
from pages import uam_roleassign_page
from pages.uam_roleassign_page import Uamroleassign
from pages.login_page import LoginPage
from context.config import settings

uam_roleassign_page = Uamroleassign.get_instance()


@given('I load the uam website')
def load_website(context):
    driver.navigate(settings.uam_url)
    driver.get_driver().maximize_window()


@when('Provide the username <username> and password <password>')
def provide_credentials(context):
    username = settings.username
    password = settings.password
    login_page = LoginPage.get_instance()
    login_page.enter_username(username)
    login_page.click_on_next_button()
    login_page.enter_password(password)


@when('Click on the Login button')
def click_sign_button(context):
    login_page = LoginPage.get_instance()
    login_page.click_on_signin_button()
    login_page.click_on_no_button()


# uam_roleassign_page.click_on_selectuser_button()


@then('Login is successful and uam page is loaded and verified')
def step_verify_login(context):
    # uam_roleassign_page = Uamroleassign.get_instance()
    page_title = uam_roleassign_page.get_page_titleofuam()
    driver.get_driver()
    time.sleep(5)
    #  driver.take_screenshot(context.scenario)
    time.sleep(5)
    try:
        assert page_title == "Trinity Solar - Application Admin", "Failed to load OneButton dashboard."
    except AssertionError:
        driver.take_screenshot(context.scenario)
        raise


@then('Navigate to Apps menu and Click on one-button redesign')
def step_navigate_to_app(context):
    # uam_roleassign_page = Uamroleassign.get_instance()
    uam_roleassign_page.click_on_applink()
    time.sleep(3)
    uam_roleassign_page.click_on_onebuttonredesignlink()
    time.sleep(5)


@then('Drag and Drop a user from Wolf_Admin to Sales-Rep')
def step_drag_and_drop(context):
    # uam_roleassign_page = Uamroleassign.get_instance()  # create an instance of the class
    uam_roleassign_page.draganddropof_userroles()


@then(u'Confirm the Role details and Click on Save.')
def step_impl(context):
    uam_roleassign_page.click_on_popup()

