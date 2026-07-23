from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

# Maximize Browser Window
driver.maximize_window()

# Wait up to 20 seconds
wait = WebDriverWait(driver, 20)

# Open Website
driver.get("https://demoqa.com/upload-download")

# Change this path to your file location
file_path = r"C:\Users\WIN11\Desktop\TestFile.txt"

# Check whether file exists
if os.path.exists(file_path):

    # Locate Upload Button
    upload = wait.until(
        EC.presence_of_element_located((By.ID, "uploadFile"))
    )

    # Upload File
    upload.send_keys(file_path)

    # Verify Uploaded File
    uploaded = wait.until(
        EC.presence_of_element_located((By.ID, "uploadedFilePath"))
    )

    print("-------------------------------------")
    print("FILE UPLOAD TEST")
    print("-------------------------------------")
    print("Uploaded File :", uploaded.text)
    print("PASS - File Uploaded Successfully")

else:
    print("FAIL - File Not Found")
    print("Expected File Path :", file_path)

# Wait for 20 seconds
time.sleep(20)

# Close Browser
driver.quit()