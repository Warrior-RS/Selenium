from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

## Solve the mathematical task

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")  # pick up the value
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")  # enter the calculated value
    input.send_keys(y)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:

    time.sleep(15)

    browser.quit()
