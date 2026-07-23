from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

# Maximize Browser
driver.maximize_window()

# Wait up to 20 seconds
wait = WebDriverWait(driver, 20)

# Open Website
driver.get("https://www.saucedemo.com/")

# Login
wait.until(
    EC.presence_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()

# Wait until inventory page loads
wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
)

# Select Price Low to High
sort = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
sort.select_by_visible_text("Price (low to high)")

print("PASS")
print("Products sorted successfully by Price (low to high).")

# Count Products
products = driver.find_elements(By.CLASS_NAME, "inventory_item")

print("Total Products :", len(products))

# Display Product Names
for product in products:
    name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    print(name)

# Wait for 20 seconds
time.sleep(20)

# Close Browser
driver.quit()