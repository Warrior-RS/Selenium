#     http://suninjuly.github.io/explicit_wait2.html
#Task: waiting for the right text on the page
#Now let's try to write a program that will book our holiday home at a strictly set price. A higher price is not good enough, and someone else will book the property at a lower price.

#In this task you have to write a program that will execute the following scenario:

#Open the page http://suninjuly.github.io/explicit_wait2.html
#Wait until the price of the house goes down to $100 (wait at least 12 seconds)
#Click on the "Book" button.
#Solve the math problem we already know (use the code you wrote earlier) and submit the solution
#To determine the moment when the rental price drops to $100, use text_to_be_present_in_element method from expected_conditions library.


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
