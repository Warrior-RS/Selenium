from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys("text")

    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    #  time delay 15 sec
    time.sleep(15)
    # close the browser after all manipulations
    browser.quit()

# don't forget to leave a blank line at the end of the file