from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

# Set up options for headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Avoid sandboxing issues
chrome_options.add_argument("--disable-dev-shm-usage")  # Workaround for low-memory environments
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
chrome_options.add_argument("--remote-debugging-port=9222")  # For debugging purposes

# Debugging: Check if chromium or chrome is available
chrome_binary_path = "/usr/bin/chromium-browser"  # For Render environments (adjust if necessary)
if os.path.exists(chrome_binary_path):
    print(f"Using Chromium binary at {chrome_binary_path}")
    chrome_options.binary_location = chrome_binary_path
else:
    print("Chromium binary not found, using default Chrome binary.")

# Use webdriver-manager to automatically download and configure ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def review(link):
    try:
        # Navigate to the website
        driver.get(f"https://www.chess.com/login_and_go?returnUrl={link}")

        # Wait for the page to load
        time.sleep(2)

        print("Filling Form")

        # Find form fields and fill them
        name_field = driver.find_element(By.XPATH, "//input[@type='email']")
        email_field = driver.find_element(By.XPATH, "//input[@type='password']")

        name_field.send_keys("Daksh_DAGGER")
        email_field.send_keys("Daksh290110")

        # Submit the form
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

        # Wait for the result page to load
        time.sleep(3)

    finally:
        # Close the browser
        driver.quit()
        print("Done")
