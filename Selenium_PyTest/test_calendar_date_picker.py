from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

# Maximize Browser Window
driver.maximize_window()

# Wait up to 20 seconds
wait = WebDriverWait(driver, 20)

# Open Website
driver.get("https://jqueryui.com/datepicker/")

# Switch to the iframe containing the date picker
wait.until(
    EC.frame_to_be_available_and_switch_to_it(
        (By.CLASS_NAME, "demo-frame")
    )
)

# Open Calendar
date_box = wait.until(
    EC.element_to_be_clickable((By.ID, "datepicker"))
)

date_box.click()

# -----------------------------
# Select Tomorrow's Date
# -----------------------------

tomorrow = datetime.now() + timedelta(days=1)
tomorrow_day = str(tomorrow.day)

future_date = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, f"//a[text()='{tomorrow_day}']")
    )
)

future_date.click()

selected_date = driver.find_element(By.ID, "datepicker").get_attribute("value")

print("--------------------------------")
print("CALENDAR DATE PICKER TEST")
print("--------------------------------")
print("Selected Date :", selected_date)

if selected_date != "":
    print("PASS - Future Date Selected Successfully")
else:
    print("FAIL - Future Date Selection Failed")

# -----------------------------
# Check Yesterday's Date
# -----------------------------

date_box.click()

yesterday = datetime.now() - timedelta(days=1)
yesterday_day = str(yesterday.day)

past_dates = driver.find_elements(
    By.XPATH,
    f"//a[text()='{yesterday_day}']"
)

if len(past_dates) == 0:
    print("PASS - Past Date Cannot Be Selected")
else:
    print("NOTE - Demo website allows past dates.")
    print("In a real interview scheduling system, past dates should be disabled.")

# Wait for 20 seconds
time.sleep(20)

# Close Browser
driver.quit()