from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

# Maximize Browser Window
driver.maximize_window()

# Wait up to 20 seconds
wait = WebDriverWait(driver, 20)

# Open Website
driver.get("https://the-internet.herokuapp.com/")

# Wait until all links are loaded
wait.until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
)

# Get all hyperlinks
links = driver.find_elements(By.TAG_NAME, "a")

print("--------------------------------------")
print("BROKEN LINK VALIDATION")
print("--------------------------------------")
print("Total Links Found:", len(links))
print()

broken_links = 0
working_links = 0

for link in links:

    url = link.get_attribute("href")

    if url is None or url == "":
        continue

    try:
        response = requests.get(url, timeout=10)

        print("URL:", url)
        print("Status Code:", response.status_code)

        if response.status_code >= 400:
            print("Result : BROKEN LINK\n")
            broken_links += 1
        else:
            print("Result : WORKING LINK\n")
            working_links += 1

    except Exception as e:
        print("URL:", url)
        print("ERROR:", e)
        print()
        broken_links += 1

print("--------------------------------------")
print("SUMMARY")
print("--------------------------------------")
print("Working Links :", working_links)
print("Broken Links  :", broken_links)

if broken_links == 0:
    print("PASS - No Broken Links Found")
else:
    print("FAIL - Broken Links Detected")

# Wait for 20 seconds
time.sleep(20)

# Close Browser
driver.quit()