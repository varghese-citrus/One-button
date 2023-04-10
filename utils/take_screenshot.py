import datetime
import os
from selenium import webdriver


def take_screenshot(context, filename):
    """
    Takes a screenshot of the current page and saves it to the specified file.

    Args:
        context: The Behave context object.
        filename: The filename to save the screenshot to.
    """
    # Ensure the screenshots directory exists
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # Create a screenshot filename with the current scenario name and timestamp
    scenario_name = context.scenario.name.replace(" ", "_")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"{scenario_name}_{timestamp}.png"

    # Take the screenshot and save it to the screenshots directory
    screenshot_path = os.path.join("screenshots", screenshot_filename)
    context.driver.save_screenshot(screenshot_path)
