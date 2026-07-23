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

# Open Student Management System
driver.get("http://127.0.0.1:5000")

# ------------------------------
# Add First Student
# ------------------------------

wait.until(
    EC.presence_of_element_located((By.ID, "usn"))
).send_keys("1BM22CS101")

driver.find_element(By.ID, "name").send_keys("Abhijith")

driver.find_element(By.ID, "department").send_keys("Computer Science")

driver.find_element(By.ID, "submit").click()

print("First Student Added Successfully")

time.sleep(2)

# ------------------------------
# Add Duplicate Student
# ------------------------------

driver.find_element(By.ID, "usn").clear()
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "department").clear()

driver.find_element(By.ID, "usn").send_keys("1BM22CS101")
driver.find_element(By.ID, "name").send_keys("Rahul")
driver.find_element(By.ID, "department").send_keys("Computer Science")

driver.find_element(By.ID, "submit").click()

# ------------------------------
# Verify Error Message
# ------------------------------

error = wait.until(
    EC.presence_of_element_located((By.ID, "error"))
).text

print("--------------------------------")
print("DUPLICATE RECORD TEST")
print("--------------------------------")
print("Error Message :", error)

if "already exists" in error.lower():
    print("PASS - Duplicate Record Rejected")
else:
    print("FAIL - Duplicate Record Accepted")

# Wait 20 Seconds
time.sleep(20)

driver.quit()