from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Set up options for headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

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
