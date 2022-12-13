from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Your code that fills in the required fields
    element = browser.find_element(By.NAME, "firstname")
    element.send_keys("Anton")
    element = browser.find_element(By.NAME, "lastname")
    element.send_keys("Klennitski")
    element = browser.find_element(By.NAME, "email")
    element.send_keys("Anton@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))            # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'Downloading files.py')           # добавляем к этому пути имя файла

    choose_file = browser.find_element(By.ID, "file")
    choose_file.send_keys(file_path)

    finalclick = browser.find_element(By.XPATH, "/html/body/div/form/button")
    finalclick.click()



finally:


    time.sleep(5)

    browser.quit()


