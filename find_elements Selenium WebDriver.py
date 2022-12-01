from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input")  #Looking for all items with selector 'input'
    for element in elements:
        element.send_keys("text")                               #Add some 'text' to the found fields

    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    #  Time delay 15 sec
    time.sleep(15)
    # Close the browser after all manipulations
    browser.quit()

# Don't forget to leave a blank line at the end of the file
