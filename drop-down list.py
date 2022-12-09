import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(int(x)+int(y))        #add up the two values

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')

    first_number = browser.find_element(By.CSS_SELECTOR, "#num1")       #find the value of the first number
    second_number = browser.find_element(By.CSS_SELECTOR, "#num2")      #find the value of the second number

    x = first_number.text       #The "text" attribute returns the text that is between the opening and closing tags of the element.
    y = second_number.text

    z = calc(x)     #number to be selected from the list

    input = browser.find_element(By.TAG_NAME, "select")     #"TAG_NAME" searches the text between two tags
    input.send_keys(z)                                      

    finalclick = browser.find_element(By.TAG_NAME, "button")    #search for and press the button
    finalclick.click()

finally:

    time.sleep(10)

    browser.quit()


