
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"                      #Go to the page


try:
    browser = webdriver.Chrome()
    browser.get(link)



    Math = str(math.ceil(math.pow(math.pi, math.e)*10000))                #searching for the right address using a mathematical function
    link = browser.find_element(By.LINK_TEXT, Math)
    link.click()

    input1 = browser.find_element(By.XPATH, "//div[1]/input")              #search by Xpath
    input1.send_keys("Anton")
    input2 = browser.find_element(By.NAME, "last_name")                    #search by Name
    input2.send_keys("Klennitski")
    input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.city')   #search by CSS Selector
    input3.send_keys("Warsaw")
    input4 = browser.find_element(By.ID, "country")                        #search by ID
    input4.send_keys("Poland")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:

    time.sleep(15)                                                          #delay time

    browser.quit()

