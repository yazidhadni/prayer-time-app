import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from functools import wraps


def driver_decorator(func):
    """
    A decorator function for setting up and managing the Chrome WebDriver.

    This decorator initializes the Chrome driver with headless mode and navigates
    to a specified URL. It wraps the decorated function, executes it, and then quits
    the Chrome driver to clean up resources.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Set up Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        # Initialize the Chrome driver
        chromedriver = webdriver.Chrome(options=chrome_options)

        mosque_id = "grande-mosquee-de-paris"
        # Navigate to the URL
        url = "https://mawaqit.net/en/" + mosque_id

        try:
            # Wait for the page to load implicitly (for js)
            chromedriver.implicitly_wait(3)
            chromedriver.get(url=url)

        except Exception as e:
            print(f"An error occured when trying to get the url: {e}")
            # Exit the script with a non-zero exit code
            sys.exit(1)

        result = func(chromedriver, *args, **kwargs)
        # Quit the Chrome driver
        chromedriver.quit()
        return result

    return wrapper
