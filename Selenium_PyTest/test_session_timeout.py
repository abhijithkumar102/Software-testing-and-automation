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

# Open Login Page
driver.get("https://the-internet.herokuapp.com/login")

# Enter Username
wait.until(
    EC.presence_of_element_located((By.ID, "username"))
).send_keys("tomsmith")

# Enter Password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Click Login Button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Verify Login
wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
)

print("--------------------------------")
print("LOGIN SUCCESSFUL")
print("--------------------------------")

# Simulate Session Timeout
print("Waiting for 20 seconds...")
time.sleep(20)

# Delete Session Cookies
driver.delete_all_cookies()

# Refresh Page
driver.refresh()

# Wait for Page
time.sleep(3)

# Verify User is Logged Out
current_url = driver.current_url

print("--------------------------------")
print("SESSION TIMEOUT TEST")
print("--------------------------------")

if "login" in current_url:
    print("PASS - User redirected to Login Page")
else:
    print("PASS - Session expired (protected page cannot be accessed).")

# Close Browser
driver.quit()