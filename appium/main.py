from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options

def run_automation():
    try:
        # Define Appium capabilities correctly
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "emulator-5554"
        options.platform_version = "15"  # Ensure this is correct
        options.automation_name = "UiAutomator2"
        options.no_reset = True

        # Start Appium session
        print("Starting Appium session...")
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
        wait = WebDriverWait(driver, 10)  # Define wait here

        # Run the automation steps
        open_app(driver, wait)
        click_confirm_button(driver, wait)
        # enter_number(driver, wait, "9125369468")
        # enter_psw(driver, wait, "dxfgdf1111")
        log_in_btn(driver, wait)
        click_task_image(driver, wait)
        click_view_element(driver, wait)
        
        
        

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        if 'driver' in locals():
            try:
                driver.quit()
                print("Driver session ended")
            except Exception as e:
                print(f"Error closing driver session: {str(e)}")

def open_app(driver, wait):
    try:
        # Try clicking the app icon
        dte_app = wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Predicted app: DTE Creative"]')
        ))
        dte_app.click()
        print("DTE Creative app opened successfully!")

    except Exception as e:
        print(f"Error finding DTE Creative app: {str(e)}")
    
def click_confirm_button(driver, wait):
    try:
        confirm_button = wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH, '//android.widget.Button[@text="Confirm"]')
        ))
        confirm_button.click()
        print("Confirm button clicked successfully!")
    except Exception as e:
        print(f"Could not find the confirm button: {str(e)}")

def enter_number(driver, wait, mobile_number):
    
    try:
        number_input = wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH,"//android.webkit.WebView[@text=\"DTE\"]/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.EditText")
        ))  # Update the `resource-id`
        number_input.send_keys(mobile_number)
        print("Number entered successfully!")
    except Exception as e:
        print(f"Could not find the number input: {str(e)}")

def enter_psw(driver, wait, password):
    try:
        password_input = wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.webkit.WebView[@text=\"DTE\"]/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.EditText')
        ))  # Update the `resource-id`
        password_input.send_keys(password)
        print("Password entered successfully!")
    except Exception as e:
        print(f"Could not find the password input: {str(e)}")

def log_in_btn(driver, wait):
    try:
        login_button = wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH, '//android.widget.Button[@text="Log in now"]')
        ))
        login_button.click()
        print("Login button clicked successfully!")
    except Exception as e:
        print(f"Could not find the login button: {str(e)}")
        
# mobile testing
def click_dte_creative(driver, wait):
    try:
        dte_app = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "DTE Creative")
        ))
        dte_app.click()
        print("DTE Creative app clicked successfully!")
    except Exception as e:
        print(f"Could not find DTE Creative app: {str(e)}")
# confirm btn
def click_button(driver, wait):
    try:
        button = wait.until(EC.element_to_be_clickable(
            (AppiumBy.CLASS_NAME, "android.widget.Button")
        ))
        button.click()
        print("Button clicked successfully!")
    except Exception as e:
        print(f"Could not find the button: {str(e)}")

def click_login_now(driver, wait):
    try:
        login_button = wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH, '//android.widget.Button[@text="Log in now"]')
        ))
        login_button.click()
        print("Login now button clicked successfully!")
    except Exception as e:
        print(f"Could not find the login now button: {str(e)}")

def click_task_image(driver, wait):
    try:
        task_image = wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH, '//android.widget.Image[@text="Task"]')
        ))
        task_image.click()
        print("Task image clicked successfully!")
    except Exception as e:
        print(f"Could not find the task image: {str(e)}")

def click_view_element(driver, wait):
    try:
        view_element = wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH, '//android.webkit.WebView[@text="DTE"]/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]')
        ))
        view_element.click()
        print("View element clicked successfully!")
    except Exception as e:
        print(f"Could not find the view element: {str(e)}")

def click_widget_button(driver, wait):
    try:
        widget_button = wait.until(EC.element_to_be_clickable(
            (AppiumBy.CLASS_NAME, "android.widget.Button")
        ))
        widget_button.click()
        print("Widget button clicked successfully!")
    except Exception as e:
        print(f"Could not find the widget button: {str(e)}")

if __name__ == "__main__":
    run_automation()
