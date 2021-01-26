import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope = "function")
def browser():
    print("\nstart test session...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit from test browser...")
    browser.quit()

@pytest.mark.parametrize('url_part', ["236895", "236896", "236897", "236898", "236899","236903", "236904", "236905"])
class Test_UFO:
    def test_link_1(self, url_part, browser):
        link = f"https://stepik.org/lesson/{url_part}/step/1"
        browser.get(link)
        answer = math.log(int(time.time()))
        browser.implicitly_wait(5)
        input1 = browser.find_element(By.CSS_SELECTOR, ("textarea.textarea"))
        input1.send_keys(str(answer))
        input2 = browser.find_element(By.CLASS_NAME, ("submit-submission"))
        input2.click()
        input3 = browser.find_element(By.CLASS_NAME, ("smart-hints__hint"))
        answer1 = input3.text
        assert answer1 == "Correct!" , \
        "Answer shoul be Correct!"
        print(answer1)


