
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))                            #calc() рассчитает и вернет значение функции, которое нужно ввести в текстовое поле.

link = "http://suninjuly.github.io/execute_script.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("window.scrollBy(0, 100);")

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")              #забераем значение
    x = x_element.text
    y = calc(x)

    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")                    #вводим посчитанное значение
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
