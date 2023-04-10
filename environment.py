from context.driver import driver
import datetime
import os
import allure
from selenium import webdriver


def after_all(context):
    driver.stop_instance()


def before_scenario(context, scenario):
    driver.clear_cookies()


# Initialize the WebDriver instance
def before_all(context):
    context.driver = webdriver.Chrome()


