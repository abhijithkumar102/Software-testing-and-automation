from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

# Maximize Browser
driver.maximize_window()

# Wait up to 20 seconds
wait = WebDriverWait(driver, 20)

# Open Website
driver.get("https://opensource-demo.orangehrmlive.com/")

# Login as Admin
wait.until(
    EC.presence_of_element_located((By.NAME, "username"))
).send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(
    By.CSS_SELECTOR,
    "button[type='submit']"
).click()

# Wait until Dashboard loads
wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//h6[text()='Dashboard']")
    )
)

print("--------------------------------")
print("ADMIN LOGIN SUCCESSFUL")
print("--------------------------------")

# Click Admin Menu
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Admin']")
    )
).click()

# Wait for User Management Page
wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//h6[text()='User Management']")
    )
)

print("PASS - Admin can access User Management")

print("--------------------------------")
print("ROLE BASED ACCESS TEST")
print("--------------------------------")
print("Admin Access : SUCCESS")

# Wait for 20 Seconds
time.sleep(20)

driver.quit()