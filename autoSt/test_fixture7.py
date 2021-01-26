import pytest
from selenium import webdriver

@pytest.fixture(scope = "function")
def bro():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(bro, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    bro.get(link)
    bro.find_element_by_css_selector("#login_link")