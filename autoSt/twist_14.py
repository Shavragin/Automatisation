from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    input1 = browser.find_element(By.ID, ("book"))
    input1.click()
    input2 = browser.find_element(By.ID, ("input_value"))
    value = input2.text
    answer = calc(value)
    input3 = browser.find_element(By.ID, ("answer"))
    input3.send_keys(answer)
    input4 = browser.find_element(By.ID, ("solve"))
    input4.click()
    #alert = browser.switch_to.alert
finally:
    time.sleep(10)
    browser.quit()



