from behave import given, when, then
from context.config import settings
from context.driver import driver

"""Common hooks for any scenario"""


@given(u'I load the website')
def load_website(context):
    driver.navigate(settings.url)
    driver.get_driver().maximize_window()


@then("Close the browser")
def step_impl(context):
    driver.browser_quit()
