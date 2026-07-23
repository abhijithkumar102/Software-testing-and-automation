from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
driver.get("https://demo.automationtesting.in/Register.html")

# First Name
wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))
).send_keys("Abhijith")

# Last Name
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Kumar")

# Address
driver.find_element(By.TAG_NAME, "textarea").send_keys("Bangalore, Karnataka")

# Email
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("abhijith@gmail.com")

# Phone
driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("9876543210")

# Gender
driver.find_element(By.XPATH, "//input[@value='Male']").click()

# Hobby
driver.find_element(By.ID, "checkbox1").click()

# Skills
skills = Select(driver.find_element(By.ID, "Skills"))
skills.select_by_visible_text("Python")

# -------- Select2 Country Dropdown --------
driver.find_element(By.XPATH, "//span[@role='combobox']").click()

search = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='search']"))
)

search.send_keys("India")
time.sleep(2)
search.send_keys(Keys.ENTER)

# -------- Date of Birth --------
year = Select(driver.find_element(By.ID, "yearbox"))
year.select_by_visible_text("2003")

month = Select(driver.find_element(By.XPATH, "//select[@placeholder='Month']"))
month.select_by_visible_text("August")

day = Select(driver.find_element(By.ID, "daybox"))
day.select_by_visible_text("18")

# Password
driver.find_element(By.ID, "firstpassword").send_keys("Password@123")

# Confirm Password
driver.find_element(By.ID, "secondpassword").send_keys("Password@123")

print("Registration Form Filled Successfully")

# Wait for 20 seconds
time.sleep(20)

# Close Browser
driver.quit()