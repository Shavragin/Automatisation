from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    found1 = browser.find_element(By.CSS_SELECTOR,("h2  :nth-child(2)"))
    value1 = found1.text
    found2 = browser.find_element(By.CSS_SELECTOR,("h2  :nth-child(4)"))
    value2 = found2.text
    summint = int(value1) + int(value2)
    summstr = str(summint)
    select = Select(browser.find_element(By.ID,("dropdown")))
    select.select_by_visible_text(summstr)
    input5 = browser.find_element(By.CLASS_NAME,("btn.btn-default"))
    input5.click()
finally:
    time.sleep(10)
    browser.quit()
