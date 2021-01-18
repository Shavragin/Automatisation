from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    value1 = browser.find_element(By.ID,("input_value"))
    x = value1.text
    fun1 = calc(x)
    browser.execute_script('window.scrollBy(0,100);')
    input1 = browser.find_element(By.ID,("answer"))
    input1.send_keys(fun1)
    input2 = browser.find_element(By.ID,("robotCheckbox"))
    input2.click()
    input3 = browser.find_element(By.ID,("robotsRule"))
    input3.click()
    input4 = browser.find_element(By.CLASS_NAME,("btn.btn-primary"))
    input4.click()
finally:
    time.sleep(10)
    browser.quit()











