from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    # link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Your code that fills in the required fields
    element = browser.find_element(By.CSS_SELECTOR, ".first_class input[required]")
    element.send_keys("Anton")
    element = browser.find_element(By.CSS_SELECTOR, ".second_class input[required]")
    element.send_keys("Klennitski")
    element = browser.find_element(By.CSS_SELECTOR, ".third_class input[required]")
    element.send_keys("Anton@gmail.com")

    # Send in the completed form
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Waiting for the page to load
    time.sleep(1)

    # find the element containing the text
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # we write in a variable "welcome_text" text from the element "welcome_text_elt"
    welcome_text = welcome_text_elt.text

    # use "assert" to check that the expected text is the same as the text on the site page
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # waiting to visually evaluate the results of the script
    time.sleep(10)
    # close the browser after all manipulations
    browser.quit()