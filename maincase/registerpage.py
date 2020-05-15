# coding=utf-8
'''
Project:页面基本操作方法
'''
from selenium.webdriver.common.by import By
from operate.basepage import BasePage
import random


# 继承BasePage类
class RegisterPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    phone_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/span/input')
    Verification_Code_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/span/input')
    Verification_Code = '000123'
    next_loc_btn = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[1]')
    name_loc_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/input')
    pwd_loc_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/input')
    re_pwd_loc_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[2]/input')
    # 团队名称
    team_loc_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/input')
    # 成员规模
    scale_loc_select = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[2]/div/input')
    scale_loc_nums = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[3]/input')
    # 使用时长
    month_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[4]/input')
    # 提交
    submit_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[1]')
    # 订单信息TEXT
    order_info_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[1]/h2')
    # 电汇转账
    Under_line_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/label/span[2]')
    # 支付宝
    on_line_zhifubao_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[1]/div/div/label[1]/span[1]/span')
    # 微信
    on_line_WeChat_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[1]/div/div/label[2]/span[1]')
    # order页面下一步按钮
    order_next_loc_btn = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]')
    # 确认支付页面-确认按钮-支付宝
    zhifu_loc_btn = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]')
    # 确认支付页面-二维码-微信
    zhifu_img_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[3]/img')
    # 线下支付-上传凭证按钮
    Upload_file = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div')
    Upload_file_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/input')

    url = "https://uat.zeropartner.com/smartfront/#/account/register"

    # 打开URL
    def open(self):
        self._open(self.url)

    # 输入验证码
    def send_Verification_Code(self):
        self.clear_and_sendkeys(self.Verification_Code, self.Verification_Code_loc)

    # 随机选择成员规模，大于30会输入人数
    def scale_select_choice(self):
        self.click_element(self.scale_loc_select)
        num = 2
        scale_loc = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[{}]/span'.format(num))
        self.wait()
        self.click_element(scale_loc)
        if num != 1:
            self.clear_and_sendkeys(random.randint(100, 2000), self.scale_loc_nums)

    # 随机月份
    def rabdom_month_send(self):
        self.clear_and_sendkeys(random.randint(3, 36), self.month_loc)

    # 企业名称
    def name_send(self):
        self.clear_and_sendkeys('测试团队{}'.format(random.randint(1, 1000)), self.team_loc_input)

    def order_next_btn_click(self):
        self.click_element(self.order_next_loc_btn)

    def to_Upload_file(self):
        self.focus_element(self.Upload_file)

    # 上传只能用绝对路径
    def upload_file_input(self):
        self.input_sendkeys('D:\PY_DEMO_1\zhixun\img\\2.jpg', self.Upload_file_input)
