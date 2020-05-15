import unittest
from maincase.loginpage import LoginPage
from selenium import webdriver


class Test_Tab(unittest.TestCase):
    """首页TAB切换测试"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.url = "https://uat.zeropartner.com/smarthome/"
        self.login_page = LoginPage(self.driver, self.url)

    def tearDown(self):
        self.driver.quit()

    def test_introduction(self):
        "平台介绍"
        self.login_page.open()
        self.login_page.click_element(self.login_page.tab_introduction_loc)

        self.assertEqual(self.driver.current_url, 'https://uat.zeropartner.com/smarthome/introduction')
    #
    # def test_businesscase(self):
    #     "行业案例"
    #     self.login_page.open()
    #     self.login_page.click_element(self.login_page.tab_businesscase_loc)
    #
    #     self.assertEqual(self.driver.current_url, 'https://uat.zeropartner.com/smarthome/businesscase')
    #
    # def test_helpcenter(self):
    #     "帮助中心"
    #     self.login_page.open()
    #     self.login_page.click_element(self.login_page.tab_helpcenter_loc)
    #     self.login_page.wait()
    #
    #     self.assertEqual(self.driver.current_url, 'https://uat.zeropartner.com/smarthome/helpcenter')


if __name__ == '__main__':
    unittest.main()
