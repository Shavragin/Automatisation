import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link= "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, ("firstname"))
    input1.send_keys("Putin")
    input2 = browser.find_element(By.NAME, ("lastname"))
    input2.send_keys("Mol")
    input3 = browser.find_element(By.NAME, ("email"))
    input3.send_keys("aaa@lll.ru")
    dir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(dir, 'fileLOL.txt')
    send_file = browser.find_element(By.ID, ("file"))
    send_file.send_keys(path)
    input4 = browser.find_element(By.CLASS_NAME, ("btn.btn-primary"))
    input4.click()
finally:
    time.sleep(10)
    browser.quit()
