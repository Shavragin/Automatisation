import pytest
from selenium import webdriver
link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():

    @classmethod
    def setup_class(cls):
        print("\n start browser for test suite 1 ..")
        cls.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        print("quit browser for test suite 1 ..")
        cls.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    class TestMainPage2():
        def setup_method(self):
            print("start browser for test 2..")
            self.browser = webdriver.Chrome()

        def teardown_method(self):
            print("quit browser for test 2..")
            self.browser.quit()

        def test_guest_should_see_login_link(self):
            print('start test link 2')
            self.browser.get(link)
            self.browser.find_element_by_css_selector("#login_link")

        def test_guest_should_see_basket_link_on_the_main_page(self):
            print('start test basket 2')
            self.browser.get(link)
            self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")



# class Metemetika():
#     def operetion_over_ckassobj(self,x,y):
#         self.x = x
#         self.y = y
#         print(x + y)
#
#     @classmethod
#     def class_obj(cls, x, y):
#         cls.x = x
#         cls.y = y
#         print(x+y)
#
#
# lol = Metemetika()
# lol.operetion_over_ckassobj(4,6)
# lol.class_obj(5,8)