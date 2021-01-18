import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID,("input_value"))
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CLASS_NAME,("form-control"))
    input1.send_keys(y)
    input2 = browser.find_element(By.ID,("robotCheckbox"))
    input2.click()
    input3 = browser.find_element(By.ID,("robotsRule"))
    input3.click()
    input4 = browser.find_element(By.CLASS_NAME,("btn.btn-default"))
    input4.click()
finally:
    time.sleep(15)
    browser.quit()



