from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  #calc() calculates and returns the function value to be entered in the text field.

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    time.sleep(1)
    buttom = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    buttom.click()

    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)


    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")  # забераем значение
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")  # вводим посчитанное значение
    input.send_keys(y)

    finalclick = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    finalclick.click()


finally:
        time.sleep(10)

        browser.quit()
