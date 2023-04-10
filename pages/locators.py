from selenium.webdriver.common.by import By


class Locator:
    """Locator objects for finding Selenium WebElements"""

    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)


class LoginPageLocators:
    """Class for OneButton Login Page"""
    USERNAME = Locator(By.ID, "i0116")
    NEXT_BUTTON = Locator(By.ID, "idSIButton9")
    PASSWORD = Locator(By.XPATH, "//input[@name='passwd']")
    SIGN_BUTTON = Locator(By.ID, "idSIButton9")
    OK_BUTTON = Locator(By.ID, "idBtn_Back")


class UamRoleAssign:
    """Class for UAM Login Page"""
    OTHER_TITLE_TEXT = Locator(By.XPATH, "//div[@id='otherTileText']")
    # ACCOUNT_TABLE = Locator(By.XPATH, "//div[@class='table'])[1]")
    APPS_LINK = Locator(By.XPATH, "//a[contains(text(),'Apps')]")
    ONEBUTTON_REDESIGN_LINK = Locator(By.XPATH, "//a[contains(text(),'One Button Redesign')]")
    # TARGETUSER_FROM = Locator(By.XPATH, "//div[@class='card-body collapse show']//ul//li[text()='Arun K R']")
    TARGETUSER_FROM = Locator(By.XPATH, "//*[@id='5']")
    DESTINATION_TO = Locator(By.XPATH, "//*[@id='role-157']/li")
    POPUP = Locator(By.XPATH, "(//button[@type='submit'])[2]")

