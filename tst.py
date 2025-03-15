# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
	"platformName": "android",
	"appium:platformVersion": "15",
	"appium:deviceName": "emulator-5554",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub/", options=options)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Predicted app: DTE Creative")
el1.click()
el2 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
el2.click()
el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Log in now\"]")
el3.click()
el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.webkit.WebView[@text=\"DTE\"]/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]")
el4.click()
el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.webkit.WebView[@text=\"DTE\"]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]")
el5.click()

driver.quit()