# Import dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By

# function to get driver
def getUrlDriver(url):
    browser = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=browser)
    driver.get(url)
    return driver

# Function for Clicking
def click_button(driver, by, xpath):
    try:
        button = driver.find_element(by, xpath)
        button.click()
       
    except Exception as e:
        print(f"An error occurred while clicking one click button: {e}")
        
# Function for entering text        
def enter_text(driver, by, xpath, text):
    try:
        element = driver.find_element(by, xpath)
        element.send_keys(text)
       
    except Exception as e:
        print(f"An error occurred while entering text: {e}")        
 
        