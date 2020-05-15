from selenium.webdriver.common.by import By
from operate.basepage import BasePage
import random


# 继承BasePage类
class HomePage(BasePage):
    # 定位器，通过元素属性定位元素对象
    # 团队名称
    team_loc_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[1]/input')
    # 成员规模
    scale_loc_select = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/input')

    scale_loc_nums = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[3]/input')
    # 使用时长
    month_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[4]/input')
    # 提交
    submit_loc_btn = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]')
    # 取消
    cancel_loc_btn = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]')

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
    order_cancel_loc_btn = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]')
    # 确认支付页面-确认/付款按钮-支付宝
    zhifu_loc_btn = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]')
    # 申请开票
    Application_invoice_btn = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div')
    # 个人
    person_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[4]/div/div[2]/div/form/div[1]/div/div/label[3]/span[2]')
    # 发票抬头
    person_taitou_loc_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div[4]/div/div[2]/div/form/div[2]/div/div/input')
    # 联系人
    person_linkman_loc_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div[4]/div/div[2]/div/form/div[3]/div/div/input')
    # 联系方式
    person_phone_loc_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div[4]/div/div[2]/div/form/div[4]/div/div/input')
    # 邮寄地址
    person_address_loc_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div[4]/div/div[2]/div/form/div[5]/div/div/input')

    # 企业普通发票
    company_common_loc = (
        By.XPATH, '//*[@id="app"]/div/div[2]/div[4]/div/div[2]/div/form/div[1]/div/div/label[2]/span[2]')

    # company_common = ['发票抬头','税号','联系人','联系方式','邮寄地址','账户号','账户名称','开户行']
    # _loc_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div[4]/div/div[2]/div/form/div[2]/div/div/input')
    # 企业增值税发票
    company_added_value_loc = (
        By.XPATH, '//*[@id="app"]/div/div[2]/div[4]/div/div[2]/div/form/div[1]/div/div/label[1]/span[2]')
    # 返回
    return_loc_btn = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[3]')
    # 删除订单
    delete_loc_btn = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[4]')

    # 确认支付页面-二维码-微信
    zhifu_img_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[3]/img')
    # 线下支付-上传凭证按钮
    Upload_file = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div')
    Upload_file_input = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/input')

    url = "https://uat.zeropartner.com/smartfront/#/account/register"

    # 打开URL
    def open(self):
        self._open(self.url)

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
