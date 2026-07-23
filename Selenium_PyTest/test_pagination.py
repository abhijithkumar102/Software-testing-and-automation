from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

# Maximize Browser Window
driver.maximize_window()

# Wait up to 20 seconds
wait = WebDriverWait(driver, 20)

# Open Website
driver.get("https://datatables.net/examples/basic_init/zero_configuration.html")

# Wait until table is loaded
wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//table[@id='example']/tbody/tr")
    )
)

# -----------------------------
# Read Page 1 Records
# -----------------------------
page1_rows = driver.find_elements(
    By.XPATH,
    "//table[@id='example']/tbody/tr/td[1]"
)

page1_names = []

for row in page1_rows:
    page1_names.append(row.text)

print("Page 1 Records")
print(page1_names)

# -----------------------------
# Go to Page 2
# -----------------------------
next_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "example_next")
    )
)

next_button.click()

# Wait for Page 2
time.sleep(3)

# -----------------------------
# Read Page 2 Records
# -----------------------------
page2_rows = driver.find_elements(
    By.XPATH,
    "//table[@id='example']/tbody/tr/td[1]"
)

page2_names = []

for row in page2_rows:
    page2_names.append(row.text)

print("\nPage 2 Records")
print(page2_names)

# -----------------------------
# Verify Records are Different
# -----------------------------
if page1_names != page2_names:
    print("\nPASS - Page 2 contains different records.")
else:
    print("\nFAIL - Same records found.")

# -----------------------------
# Verify Current Page Number
# -----------------------------
page_number = driver.find_element(
    By.CSS_SELECTOR,
    "#example_paginate span .current"
).text

print("Current Page :", page_number)

if page_number == "2":
    print("PASS - Page Number Updated Correctly")
else:
    print("FAIL - Incorrect Page Number")

# -----------------------------
# Verify Total Records
# -----------------------------
info = driver.find_element(
    By.ID,
    "example_info"
).text

print("Table Info :", info)

if "entries" in info:
    print("PASS - Total Record Count Displayed")
else:
    print("FAIL - Record Count Missing")

# Wait for 20 seconds
time.sleep(20)

# Close Browser
driver.quit()