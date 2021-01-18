from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    inptut1 = browser.find_element(By.CLASS_NAME, ("btn.btn-primary"))
    inptut1.click()
    alert = browser.switch_to.alert
    alert.accept()
    input2 = browser.find_element(By.ID, ("input_value"))
    x = input2.text
    input3 = browser.find_element(By.ID, ("answer"))
    answer = calc(x)
    input3.send_keys(answer)
    input4 = browser.find_element(By.CLASS_NAME, ("btn.btn-primary"))
    input4.click()
finally:
    time.sleep(10)
    browser.quit()
