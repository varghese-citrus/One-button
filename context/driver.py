import os
from datetime import datetime

from selenium import webdriver
from context.config import settings


class Driver(object):
    """Singleton class for interacting with the selenium webdriver object"""
    instance = None

    class SeleniumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Driver()
        return cls.instance

    def __init__(self):
        if settings.browser == "chrome":
            self.driver = webdriver.Chrome()
        elif settings.browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise Driver.SeleniumDriverNotFound(
                f"{settings.browser} not currently supported")

    def get_driver(self):
        return self.driver

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)

    def browser_quit(self):
        self.driver.quit()

    def take_screenshot(self, scenario):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        # Create a screenshot filename with the current scenario name and timestamp
        scenario_name = scenario.name.replace(" ", "_")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_filename = f"{scenario_name}_{timestamp}.png"
        # Take the screenshot and save it to the screenshots directory
        screenshot_path = os.path.join("screenshots", screenshot_filename)
        self.driver.save_screenshot(screenshot_path)


driver = Driver.get_instance()
