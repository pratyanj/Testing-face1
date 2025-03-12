from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
import random
import sys
# Set up the Selenium WebDriver

driver = webdriver.Chrome()

# for replit
# options = webdriver.ChromeOptions()
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--disable-gpu')
# service = webdriver.ChromeService()
# driver = webdriver.Chrome(options=options)


driver.get("http://dteworks01.com/xml/index.html#/login")
wait = WebDriverWait(driver, 10)

def sl(x,y):
    sleep(round(random.uniform(x, y), 2))
def login(mobile_number:str,psw:str):
    '''
    This function logs in to the website using the provided mobile number and password.
    It waits for the login button to be clickable and then scrolls to it and clicks it.
    
    args:
        mobile_number (str): The mobile number to be used for login.
        psw (str): The password to be used for login.
    '''
    phone_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Please enter your phone number']")))
    phone_input.send_keys(mobile_number)

    password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Please enter login password']")))
    password_input.send_keys(psw)

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'van-button__content')]/span[contains(text(), 'Log in now')]")))
    sl(0.5, 1)

    # Scroll to the button and click using JavaScript
    driver.execute_script("arguments[0].scrollIntoView();", login_button)
    sl(0.5, 1)
    driver.execute_script("arguments[0].click();", login_button)

def click_task():
    '''
    This function clicks on the "Task" button on the website.
    It waits for the task button to be clickable and then scrolls to it and clicks it.
    '''
    try:
        task_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='van-tabbar-item__text' and contains(text(), 'Task')]")))
        sl(0.5, 1)
        driver.execute_script("arguments[0].click();", task_button)
    except:
        print("Task button not found or not clickable.")
def click_task_item():
    try:
        
        task_item = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@style='position: relative;']//i[contains(@class, 'van-icon-play-circle-o')]")))
        sl(0.5, 1)
        driver.execute_script("arguments[0].click();", task_item)
    except:
        print("Task item not found or not clickable.")

def handle_task_completion():
    try:
        # Wait for the task completed message to appear
        task_completed_msg = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//div[@class='van-dialog__message van-dialog__message--has-title' and contains(text(), 'Task today has been completed')]")))
        print("Task completed message found")
        if task_completed_msg:
            # Wait for the 'Confirm' button and click it
            confirm_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='van-button__content']//span[contains(text(), 'Confirm')]")))
            sl(0.5, 1)  # Random delay
            driver.execute_script("arguments[0].click();", confirm_btn)
            print("Confirm button clicked")

            # Take a screenshot after confirming
            sl(0.5, 3)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='van-tabbar-item__text' and contains(text(), 'My')]")))
            sl(1, 5)
            
            # driver.save_screenshot(f"task_completed_{time.strftime('%Y%m%d')}.png")
            # print("Screenshot taken")
            close()
            quit()
    except:
        print("Timeout: Task completion message or confirm button not found.")
        

def click_play_button():
    try:
        try:
            play_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'vjs-big-play-button')]")))
        except:
            play_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "vjs-big-play-button")))
        sl(0.5, 1)
        driver.execute_script("arguments[0].click();", play_button)
    except:
        print("Play button not found.")
        click_watch_later()


def click_watch_later():
    try:
        watch_later_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='watch later']/ancestor::button")))
        sl(0.5, 1)
        driver.execute_script("arguments[0].click();", watch_later_button)
    except:
        print("Watch later button not found.")
    

def click_start_answering():
    try:
        start_answering_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Start Answering']/ancestor::button")))
        driver.execute_script("arguments[0].click();", start_answering_button)
    except:
        print("Start answering button not found.")


def description_extract():
    """
    Extracts the description text from the specified div element quickly.
    """
    try:
        # Reduce wait time for presence detection
        description_element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@style, 'background: rgb(255, 255, 255)') and contains(@style, 'border-radius: 10px')]")
            )
        )
        
        description = description_element.text.strip()
        # print(f"Extracted Description: {description}")
        return description

    except:
        print("Description element not found.")
        return None


def click_submit_answer():
    """
    Waits for and clicks the 'Submit Answer' button.
    """
    try:
        submit_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space(text())='Submit Answer']/ancestor::button")
        ))
        sl(0.5, 1)  # Random delay to mimic human interaction
        driver.execute_script("arguments[0].click();", submit_button)
        print("Clicked 'Submit Answer' button.")

    except:
        print("Submit Answer button not found or not clickable.")


def click_matching_brand(matched_brand):
    if matched_brand:
        try:
            brand_element = wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[contains(@class, 'answer') and normalize-space(text())='{matched_brand}']")
            ))
            sl(0.5, 1)
            driver.execute_script("arguments[0].click();", brand_element)
            print(f"Clicked on {matched_brand}")
        except:
            print(f"Brand {matched_brand} not found or not clickable.")
            close_answer_popup()
            click_watch_later()
def close_answer_popup():
    try:
        close_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//i[contains(@class, 'van-icon-cross') and contains(@class, 'van-popup__close-icon')]")
        ))
        sl(0.5, 2)
        driver.execute_script("arguments[0].click();", close_button)
        print("Closed answer popup.")
    except:
        print("Close button not found or not clickable.")
        
def click_back_to_next():
    try:
        back_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space(text())='Back to next']/ancestor::button")
        ))
        sl(0.5, 1)
        driver.execute_script("arguments[0].click();", back_button)
        print("Clicked 'Back to Next' button.")
    except:
        print("Back to Next button not found or not clickable.")

def close():
    try:
        driver.quit()
    except:
        print("Driver not found.")

# ---------------------------------------------------------------------------------------------------
# Work Flow
# ---------------------------------------------------------------------------------------------------
login('9157259694','200150109564')
sl(0.5, 1)
# click task page
click_task()
sleep(round(random.uniform(0.5, 1), 2))
# click first task

def play(brand:str):
    sleep(16)
    click_start_answering()
    sl(0.5, 3)
    click_matching_brand(brand)
    click_submit_answer()
    click_back_to_next()
    print('---------------------------------------------------------')
# inside while loop set task number counter
task=0
goal = 40
while True:
    if task == goal:
        break
    click_task_item()
    try:
        click_play_button()
    except:
        handle_task_completion()
    sl(0.8, 2)
    des = description_extract()
    brands = ['BVLGARI', 'Bvlgari','Bulgari', 'Gucci', 'Burberry', 'Hermès']
    matched_brand = next((name for name in brands if name in des), None)
    if matched_brand:
        if matched_brand == 'Bulgari' or matched_brand == 'BVLGARI' or matched_brand == 'Bvlgari':
            play('BVLGARI')
        elif matched_brand == 'Hermès':
            play('hermes')
        else:
            play(matched_brand)
        task+=1
        print('-----------------')
        print(f'task: {task}')
        print('-----------------')
    else:
        click_watch_later()


    
sleep(10)
close()