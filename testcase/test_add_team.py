import unittest
from maincase.loginpage import LoginPage
from selenium import webdriver
from operate.BusinessOperate import Login_Public


class Add_Team(unittest.TestCase):
    """创建团队及订单相关功能测试"""

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
        over_login = Login_Public(self.driver)
        over_login.start_login()
