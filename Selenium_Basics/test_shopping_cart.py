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
driver.get("https://www.saucedemo.com/")

# Login
wait.until(
    EC.presence_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()

# Wait until products page loads
wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
)

# Add Backpack
driver.find_element(
    By.ID,
    "add-to-cart-sauce-labs-backpack"
).click()

# Add Bike Light
driver.find_element(
    By.ID,
    "add-to-cart-sauce-labs-bike-light"
).click()

print("Two products added successfully.")

# Open Cart
driver.find_element(
    By.CLASS_NAME,
    "shopping_cart_link"
).click()

# Verify Number of Products
cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")

print("Number of Products in Cart :", len(cart_items))

if len(cart_items) == 2:
    print("PASS - Two products are available in the cart.")
else:
    print("FAIL - Cart verification failed.")

# Get Product Prices
price1 = float(
    cart_items[0].find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text.replace("$", "")
)

price2 = float(
    cart_items[1].find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text.replace("$", "")
)

total = price1 + price2

print("Product 1 Price : $", price1)
print("Product 2 Price : $", price2)
print("Calculated Total : $", total)

print("PASS - Cart total calculated successfully.")

# Wait for 20 seconds
time.sleep(20)

# Close Browser
driver.quit()