
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
#calc() calculates and returns the function value to be entered in the text field.

link = "http://suninjuly.github.io/execute_script.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("window.scrollBy(0, 100);")
    #With the execute_script method you can execute a program written in JavaScript as part of an autotest script in a running browser.
    #Note that executable JavaScript must be enclosed in quotation marks (double or single quotes).
    # If you also need to use quotation marks inside the script and you already use double quotes to select the script, you should put single quotes in the script:
    #browser.execute_script("document.title='Script executing';")

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")              ##pick up the value
    x = x_element.text
    y = calc(x)

    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")                    ##enter the calculated value
    input2.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    finalclick = browser.find_element(By.XPATH, "/html/body/div[1]/form/button")
    finalclick.click()

finally:

    time.sleep(15)
    browser.quit()
