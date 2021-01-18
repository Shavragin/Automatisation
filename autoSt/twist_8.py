from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.ID, ("treasure"))
    attr1 = input1.get_attribute("valuex")
    resolve = calc(attr1)
    input2 = browser.find_element(By.ID, ("answer"))
    input2.send_keys(resolve)
    input3 = browser.find_element(By.ID,("robotCheckbox"))
    input3.click()
    input4 = browser.find_element(By.ID,("robotsRule"))
    input4.click()
    input5 = browser.find_element(By.CLASS_NAME,("btn.btn-default"))
    input5.click()
finally:
    time.sleep(15)
    browser.quit()



