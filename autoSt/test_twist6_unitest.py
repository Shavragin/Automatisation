from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class test_bare(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, '//input[@placeholder = "Input your first name"]')
        input1.send_keys("Антон")
        input2 = browser.find_element(By.XPATH, '//input[@placeholder = "Input your last name"]')
        input2.send_keys("Петров")
        input3 = browser.find_element(By.XPATH, '//input[@placeholder = "Input your email"]')
        input3.send_keys("AAa@mail.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, welcome_text_elt.text, "Congratulations! You have successfully registered!")

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, '//input[@placeholder = "Input your first name"]')
        input1.send_keys("Антон")
        input2 = browser.find_element(By.XPATH, '//input[@placeholder = "Input your last name"]')
        input2.send_keys("Петров")
        input3 = browser.find_element(By.XPATH, '//input[@placeholder = "Input your email"]')
        input3.send_keys("AAa@mail.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, welcome_text_elt.text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()
    print("All tests is done")



