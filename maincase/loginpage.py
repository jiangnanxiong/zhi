# coding=utf-8
'''
Project:页面基本操作方法：如open，input_username，input_password，click_submit
'''
from selenium.webdriver.common.by import By
from operate.basepage import BasePage


# 继承BasePage类
class LoginPage(BasePage):
    # 首页定位器，通过元素属性定位元素对象
    login_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div/div[3]/a[1]')
    username_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div[2]/div/div[3]/form/div[1]/div/div/input')
    password_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div[2]/div/div[3]/form/div[2]/div/div/input')
    submit_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div')
    queding_loc = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')
    username = "15755170007"
    password = "123456"
    erro_text_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div[2]/div/div[2]')
    erro_text = '用户不存在/密码错误'
    tab_introduction_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div/div[2]/div[2]/a/span')
    tab_businesscase_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div/div[2]/div[3]/a/span')
    tab_helpcenter_loc = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div/div[2]/div[4]/a/span')
    url = 'https://uat.zeropartner.com/smarthome/'

    # 点击登录按钮
    def click_login_btn(self):
        self.click_element(self.login_loc)

    # 点击账号输入框，并输入
    def click_username_input(self):
        self.clear_and_sendkeys(self.username, self.username_loc)

    # 点击密码输入框，并输入
    def click_password_input(self):
        self.clear_and_sendkeys(self.password, self.password_loc)

    # 点击登录提交按钮
    def click_submit_btn(self):
        self.click_element(self.submit_loc)

    # 如果存在账户已登录情况，判断弹框确定按钮是否存在强制登录
    def click_queding_loc_btn(self):
        if self.find_element(self.queding_loc):
            self.click_element(self.queding_loc)

    # 打开URL
    def open(self):
        self._open(self.url)

    # 密码错误提示
    def find_erro_text(self):
        if self.is_page_has_text(self.erro_text):
            return True
        else:
            return False