from context.driver import driver
from pages.locators import LoginPageLocators
from pages.page import Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(Page):
    """Object to represent the one button login page"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def enter_username(self, username):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((LoginPageLocators.USERNAME.l_type, LoginPageLocators.USERNAME.selector))
        )
        element.send_keys(username)

    def click_on_next_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((LoginPageLocators.NEXT_BUTTON.l_type, LoginPageLocators.NEXT_BUTTON.selector))
        )
        element.click()

    def enter_password(self, password):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((LoginPageLocators.PASSWORD.l_type, LoginPageLocators.PASSWORD.selector))
        )
        element.clear()
        element.send_keys(password)

    def click_on_signin_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((LoginPageLocators.SIGN_BUTTON.l_type, LoginPageLocators.SIGN_BUTTON.selector))
        )
        element.click()

    def click_on_no_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((LoginPageLocators.OK_BUTTON.l_type, LoginPageLocators.OK_BUTTON.selector))
        )
        element.click()

    def get_page_title(self):
        return self.driver.title

