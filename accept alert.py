from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  #calc() calculates and returns the function value to be entered in the text field.

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    buttom1 = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    buttom1.click()

    confirm = browser.switch_to.alert       #переключаемся на всплывающее окно и соглашаемся
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")                    #enter the calculated value
    input2.send_keys(y)

    finalclick = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    finalclick.click()

finally:
    #  time delay 15 sec
    time.sleep(15)
    # close the browser after all manipulations
    browser.quit()