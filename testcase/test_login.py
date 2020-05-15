import unittest
from maincase.loginpage import LoginPage
from selenium import webdriver


class Test_login(unittest.TestCase):
    """登录功能测试"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    # 用例执行体
    def test_login_1(self):
        "正确账号密码登录"
        # 声明LoginPage类对象
        login_page = LoginPage(self.driver)
        login_page.open()
        # 调用打开页面组件
        login_page.click_login_btn()
        login_page.click_username_input()
        login_page.click_password_input()
        login_page.click_submit_btn()
        login_page.click_queding_loc_btn()
        login_page.wait()

        self.assertEqual(self.driver.current_url, 'https://uat.zeropartner.com/smartfront/#/teamlist/index')

    def test_login_2(self):
        "存在账号错误密码登录"
        # 声明LoginPage类对象
        login_page = LoginPage(self.driver)
        login_page.open()
        # 调用打开页面组件
        login_page.click_login_btn()
        login_page.click_username_input()
        login_page.clear_and_sendkeys('123', login_page.password_loc)
        login_page.click_submit_btn()

        self.assertEqual(login_page.find_erro_text(), True)


if __name__ == "__main__":
    unittest.main()
