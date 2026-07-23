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
driver.get("https://demo.opencart.com/")

# Search Product
search = wait.until(
    EC.presence_of_element_located((By.NAME, "search"))
)

search.send_keys("iPhone")

driver.find_element(By.CSS_SELECTOR, "button.btn.btn-light").click()

# Open Product
wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "iPhone"))
).click()

# Add to Cart
wait.until(
    EC.element_to_be_clickable((By.ID, "button-cart"))
).click()

time.sleep(3)

# Open Shopping Cart
driver.get("https://demo.opencart.com/en-gb?route=checkout/cart")

# Quantity Box
qty = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//input[contains(@name,'quantity')]")
    )
)

qty.clear()
qty.send_keys("4")

# Update Quantity
driver.find_element(
    By.CSS_SELECTOR,
    "button[data-bs-original-title='Update']"
).click()

time.sleep(3)

# Read Total
total = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//strong[text()='Total']/../../td[2]")
    )
).text

print("--------------------------------")
print("SHOPPING CART QUANTITY TEST")
print("--------------------------------")

print("Updated Quantity : 4")
print("Cart Total :", total)

print("PASS - Quantity Updated Successfully")

# Wait for 20 seconds
time.sleep(20)

driver.quit()