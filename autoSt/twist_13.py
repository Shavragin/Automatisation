from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CLASS_NAME, ("trollface.btn.btn-primary"))
    input1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    input2 = browser.find_element(By.ID, ("input_value"))
    x = input2.text
    answer = calc(x)
    input3 = browser.find_element(By.ID, ("answer"))
    input3.send_keys(answer)
    input4 = browser.find_element(By.CLASS_NAME, ("btn.btn-primary"))
    input4.click()
finally:
    time.sleep(10)
    browser.quit()

