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

# -------------------------------
# Click Name Column (Ascending)
# -------------------------------
name_header = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//table[@id='example']/thead/tr/th[1]")
    )
)

name_header.click()

time.sleep(2)

# Read Ascending Data
ascending_names = []

rows = driver.find_elements(
    By.XPATH,
    "//table[@id='example']/tbody/tr/td[1]"
)

for row in rows:
    ascending_names.append(row.text)

print("Ascending Order")
print(ascending_names)

# Verify Ascending Order
expected_ascending = sorted(ascending_names)

if ascending_names == expected_ascending:
    print("PASS - Ascending Sorting Successful")
else:
    print("FAIL - Ascending Sorting Failed")

# -------------------------------
# Click Again (Descending)
# -------------------------------
name_header.click()

time.sleep(2)

descending_names = []

rows = driver.find_elements(
    By.XPATH,
    "//table[@id='example']/tbody/tr/td[1]"
)

for row in rows:
    descending_names.append(row.text)

print("\nDescending Order")
print(descending_names)

# Verify Descending Order
expected_descending = sorted(descending_names, reverse=True)

if descending_names == expected_descending:
    print("PASS - Descending Sorting Successful")
else:
    print("FAIL - Descending Sorting Failed")

# Wait for 20 seconds
time.sleep(20)

# Close Browser
driver.quit()