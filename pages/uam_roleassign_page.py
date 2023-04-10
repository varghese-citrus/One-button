import time

from selenium.common import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from context.driver import driver
from pages.locators import UamRoleAssign
from pages.page import Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Uamroleassign(Page):
    """Object to represent the UAM login page"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Uamroleassign()
        return cls.instance

    def __init__(self):
        super().__init__()
        self.accept_next_alert = True

    def click_on_othertitletext(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (UamRoleAssign.OTHER_TITLE_TEXT.l_type, UamRoleAssign.OTHER_TITLE_TEXT.selector))

        )
        element.click()

    def click_on_selectuser_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (UamRoleAssign.ACCOUNT_TABLE.l_type, UamRoleAssign.ACCOUNT_TABLE.selector))

        )
        element.click()

    def click_on_applink(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (UamRoleAssign.APPS_LINK.l_type, UamRoleAssign.APPS_LINK.selector))

        )
        element.click()

    def click_on_onebuttonredesignlink(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (UamRoleAssign.ONEBUTTON_REDESIGN_LINK.l_type, UamRoleAssign.ONEBUTTON_REDESIGN_LINK.selector))

        )
        element.click()
        time.sleep(5)

    def draganddropof_userroles(self):
        ldriver = driver.get_driver()
        time.sleep(5)
        ldriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        uam_roleassign_page_from = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (UamRoleAssign.TARGETUSER_FROM.l_type, UamRoleAssign.TARGETUSER_FROM.selector))
        )
        time.sleep(5)
        uam_roleassign_page_to = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (UamRoleAssign.DESTINATION_TO.l_type, UamRoleAssign.DESTINATION_TO.selector))
        )
        # Scroll to the destination element
        ldriver.execute_script("arguments[0].scrollIntoView();", uam_roleassign_page_to)
        # Scroll up by 100 pixels
        ldriver.execute_script("window.scrollBy(0, -100);")
        time.sleep(3)
        actions = ActionChains(ldriver)
        actions.click_and_hold(uam_roleassign_page_from).perform()
        time.sleep(5)
        actions.move_to_element(uam_roleassign_page_to).perform()
        time.sleep(5)
        actions.release(uam_roleassign_page_to).perform()
        time.sleep(5)

    def click_on_popup(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (UamRoleAssign.POPUP.l_type, UamRoleAssign.POPUP.selector))

            )
            element.click()
            time.sleep(5)
        except Exception as e:
            print("An error occurred while clicking on the popup: ", str(e))

    def get_page_titleofuam(self):
        return self.driver.title
