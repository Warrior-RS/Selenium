
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/find_link_text"


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")




    input1 = browser.find_element(By.XPATH, "//div[1]/input")
    input1.send_keys("Anton")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Klennitski")
    input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
    input3.send_keys("Warsaw")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Poland")
    button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
    button.click()


finally:

    time.sleep(15)

    browser.quit()
