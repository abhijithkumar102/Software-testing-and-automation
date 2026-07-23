from selenium import webdriver
import time


def test_open_google():
    # Launch Chrome browser
    driver = webdriver.Chrome()

    try:
        # Maximize browser window
        driver.maximize_window()

        # Open Google
        driver.get("https://www.google.com")

        # Verify page title
        assert "Google" in driver.title

        print("Google page opened successfully.")
        print("Page Title:", driver.title)

        # Wait for 3 seconds
        time.sleep(3)

    finally:
        # Close browser
        driver.quit()