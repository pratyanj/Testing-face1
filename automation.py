from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def run_automation():
    # Appium Server Configuration
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        
    }

    # Start Appium session
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    
    # Open Google and search for "dtework"
    try:
        element = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@content-desc='YouTube']"))
        )
        element.click()
    except TimeoutException:
        print("Element not found within 2 minutes")
    
    # Wait for results
    time.sleep(5)

    # Quit the driver
    driver.quit()

# Run the function
run_automation()