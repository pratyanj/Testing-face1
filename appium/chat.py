from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import mainthread
from threading import Thread
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "20dp"
        
        MDTopAppBar:
            title: "Appium Automation"
            elevation: 4
            md_bg_color: app.theme_cls.primary_color
            
        ScrollView:
            MDList:
                spacing: "15dp"
                padding: "10dp"
                
                MDRaisedButton:
                    text: "Open DTE App"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": .5}
                    on_release: app.run_in_thread(app.open_app)
                    
                MDRaisedButton:
                    text: "Click Confirm Button"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": .5}
                    on_release: app.run_in_thread(app.click_confirm_button)
                    
                MDRaisedButton:
                    text: "Click Login Button"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": .5}
                    on_release: app.run_in_thread(app.log_in_btn)
                    
                MDRaisedButton:
                    text: "Click Task Image"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": .5}
                    on_release: app.run_in_thread(app.click_task_image)
                    
                MDRaisedButton:
                    text: "Click View Element"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": .5}
                    on_release: app.run_in_thread(app.click_view_element)'''

class MyApp(MDApp):
    def build(self):
        self.start_driver()  # Initialize driver when app starts
        return Builder.load_string(KV)

    def start_driver(self):
        """Start the Appium driver"""
        try:
            options = UiAutomator2Options()
            options.platform_name = "Android"
            options.device_name = "emulator-5554"  # Change to your device name
            options.automation_name = "UiAutomator2"
            options.no_reset = True

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
            self.wait = WebDriverWait(self.driver, 10)
            print("Appium session started")
        except Exception as e:
            print(f"Error starting Appium: {str(e)}")

    def run_in_thread(self, func):
        """Run function in a thread to prevent UI freezing"""
        Thread(target=func).start()

    
    def open_app(self):
        """Open DTE Creative app"""
        try:
            dte_app = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Predicted app: DTE Creative"]')
            ))
            dte_app.click()
            print("DTE Creative app opened successfully!")
        except Exception as e:
            print(f"Error finding DTE Creative app: {str(e)}")

    def click_confirm_button(self):
        """Click confirm button"""
        try:
            confirm_button = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.Button[@text="Confirm"]')
            ))
            confirm_button.click()
            print("Confirm button clicked successfully!")
        except Exception as e:
            print(f"Could not find the confirm button: {str(e)}")

    def log_in_btn(self):
        """Click login button"""
        try:
            login_button = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.Button[@text="Log in now"]')
            ))
            login_button.click()
            print("Login button clicked successfully!")
        except Exception as e:
            print(f"Could not find the login button: {str(e)}")

    def click_task_image(self):
        """Click task image"""
        try:
            task_image = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.Image[@text="Task"]')
            ))
            task_image.click()
            print("Task image clicked successfully!")
        except Exception as e:
            print(f"Could not find the task image: {str(e)}")

    def click_view_element(self):
        """Click view element"""
        try:
            view_element = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//android.webkit.WebView[@text=\"DTE\"]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]")
            ))
           
            view_element.click()
            print("View element clicked successfully!")
        except Exception as e:
            print(f"Could not find the view element: {str(e)}")

if __name__ == "__main__":
    MyApp().run()
