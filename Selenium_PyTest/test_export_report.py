from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

# Maximize Browser
driver.maximize_window()

# Wait up to 20 seconds
wait = WebDriverWait(driver, 20)

# Open Website
driver.get("https://opensource-demo.orangehrmlive.com/")

# Login
wait.until(
    EC.presence_of_element_located((By.NAME, "username"))
).send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait for Dashboard
wait.until(
    EC.presence_of_element_located((By.XPATH, "//h6"))
)

print("--------------------------------")
print("LOGIN SUCCESSFUL")
print("--------------------------------")

# -------------------------------------------------
# Example Only
# Replace this locator with your application's
# Export button if available.
# -------------------------------------------------

try:
    export_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Export')]")
        )
    )

    export_button.click()

    print("PASS - Export Button Clicked")

except:
    print("NOTE - Export button is not available in this demo website.")

# Wait for download
time.sleep(5)

# Download Folder
download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

files = os.listdir(download_folder)

excel_files = [file for file in files if file.endswith(".xlsx")]

print("--------------------------------")
print("DOWNLOAD VERIFICATION")
print("--------------------------------")

if len(excel_files) > 0:
    print("PASS - Excel File Downloaded")
    print("Downloaded File:", excel_files[-1])
else:
    print("NOTE - No Excel file found.")

# Wait 20 Seconds
time.sleep(20)

driver.quit()