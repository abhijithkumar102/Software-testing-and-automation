from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Launch Chrome
driver = webdriver.Chrome()

# Maximize Window
driver.maximize_window()

# Wait 20 Seconds
wait = WebDriverWait(driver,20)

# Open Website
driver.get("https://demoqa.com/upload-download")

# ==========================
# CHANGE THIS PATH
# ==========================

file_path = r"C:\Users\WIN11\Desktop\TestFile.txt"

# ==========================

if os.path.isfile(file_path):

    upload = wait.until(
        EC.presence_of_element_located((By.ID,"uploadFile"))
    )

    upload.send_keys(file_path)

    uploaded = wait.until(
        EC.presence_of_element_located((By.ID,"uploadedFilePath"))
    )

    print("------------------------------------")
    print("FILE UPLOAD TEST")
    print("------------------------------------")
    print(uploaded.text)
    print("PASS - File Uploaded Successfully")

else:

    print("------------------------------------")
    print("FAIL")
    print("File Not Found")
    print(file_path)

# Download File
download = wait.until(
    EC.element_to_be_clickable((By.ID,"downloadButton"))
)

download.click()

print("------------------------------------")
print("DOWNLOAD TEST")
print("------------------------------------")
print("PASS - Download Started Successfully")

time.sleep(20)

driver.quit()