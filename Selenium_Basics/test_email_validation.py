from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

driver.get("https://demo.automationtesting.in/Register.html")

# Locate Email field
email = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
)

# Enter Valid Email
email.send_keys("abhijith123@gmail.com")

# Check Validation Message
message = driver.execute_script(
    "return arguments[0].validationMessage;", email
)

if message == "":
    print("PASS")
    print("Valid email accepted.")
else:
    print("FAIL")
    print("Validation Message:", message)

# Wait for 20 seconds
time.sleep(20)

driver.quit()