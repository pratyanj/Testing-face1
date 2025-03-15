import threading
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# Import Appium WebDriver and Selenium support tools
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define your mobile automation class using Appium
class MobileAutomation:
    def __init__(self):
        # Set up desired capabilities for Android Chrome (adjust as needed)
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Android Emulator",  # Change to your device name if needed
            "browserName": "Chrome"
        }
        # Connect to the Appium server (ensure Appium server is running)
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, mobile_number: str, psw: str):
        self.driver.get("http://dteworks01.com/xml/index.html#/login")
        time.sleep(3)
        phone_input = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Please enter your phone number']")))
        phone_input.send_keys(mobile_number)
        password_input = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Please enter login password']")))
        password_input.send_keys(psw)
        login_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'van-button__content')]/span[contains(text(), 'Log in now')]")))
        login_button.click()

    def quit(self):
        self.driver.quit()

# This function runs your automation (adjust or expand as needed)
def run_automation():
    automation = MobileAutomation()
    automation.login("9157259694", "200150109564")
    time.sleep(10)  # Wait for any tasks to complete; adjust timing as needed
    automation.quit()

# Define a simple Kivy UI that starts the automation when a button is pressed
class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
        run_button = Button(text="Run Automation", size_hint=(1, 0.2))
        run_button.bind(on_press=lambda instance: threading.Thread(
            target=run_automation, daemon=True).start())
        layout.add_widget(run_button)
        return layout

if __name__ == "__main__":
    MyApp().run()

