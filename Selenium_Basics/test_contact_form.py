from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

# Maximize Browser Window
driver.maximize_window()

# Wait up to 5 minutes (300 seconds)
wait = WebDriverWait(driver, 300)

# Open the Website
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Enter Text
wait.until(EC.presence_of_element_located((By.NAME, "my-text"))).send_keys("Abhijith")

# Enter Password
wait.until(EC.presence_of_element_located((By.NAME, "my-password"))).send_keys("Abhijith@123")

# Enter Text Area
wait.until(EC.presence_of_element_located((By.NAME, "my-textarea"))).send_keys("This is a Selenium Automation Test.")

# Click the Submit Button
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))).click()

# Wait for the success message
message = wait.until(
    EC.presence_of_element_located((By.ID, "message"))
).text

# Print the Result
print("Success Message:", message)

# Pause for 5 seconds before closing
time.sleep(50)

# Close the Browser
driver.quit()