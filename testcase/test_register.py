import unittest
from maincase.registerpage import RegisterPage
from selenium import webdriver
from operate.tool import *


class Test_register(unittest.TestCase):
    """注册测试及订单支付方式选择"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.register_page = RegisterPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_newuser_register(self):
        "新用户注册-设置密码-新建企业团队生成订单"
        self.register_page.open()
        self.register_page.clear_and_sendkeys(phone_num(), self.register_page.phone_loc)
        self.register_page.send_Verification_Code()
        self.register_page.click_element(self.register_page.next_loc_btn)
        self.register_page.clear_and_sendkeys(random_name(), self.register_page.name_loc_input)
        self.register_page.clear_and_sendkeys('123456', self.register_page.pwd_loc_input)
        self.register_page.clear_and_sendkeys('123456', self.register_page.re_pwd_loc_input)
        self.register_page.click_element(self.register_page.next_loc_btn)
        self.register_page.name_send()
        self.register_page.scale_select_choice()
        self.register_page.rabdom_month_send()
        self.register_page.click_element(self.register_page.submit_loc)

        self.assertEqual(self.register_page.is_page_has_text('完成付费，开通企业/团队'), True)
        self.assertEqual(self.register_page.is_page_has_text('订单信息'), True)

    def test_newuser_register_on_line_zhifubao(self):
        "新用户注册-设置密码-新建企业团队-线上支付宝付款"
        self.register_page.open()
        self.register_page.clear_and_sendkeys(phone_num(), self.register_page.phone_loc)
        self.register_page.send_Verification_Code()
        self.register_page.click_element(self.register_page.next_loc_btn)
        self.register_page.clear_and_sendkeys(random_name(), self.register_page.name_loc_input)
        self.register_page.clear_and_sendkeys('123456', self.register_page.pwd_loc_input)
        self.register_page.clear_and_sendkeys('123456', self.register_page.re_pwd_loc_input)
        self.register_page.click_element(self.register_page.next_loc_btn)
        self.register_page.name_send()
        self.register_page.scale_select_choice()
        self.register_page.rabdom_month_send()
        self.register_page.click_element(self.register_page.submit_loc)
        self.register_page.click_element(self.register_page.on_line_zhifubao_loc)
        self.register_page.order_next_btn_click()
        # 点的太快了
        self.register_page.wait(1)
        self.register_page.click_element(self.register_page.zhifu_loc_btn)

        self.assertEqual(self.register_page.is_page_has_text('我的收银台'), True)
        self.assertIn('网上支付', self.driver.title)

    def test_newuser_register_on_line_WeChat(self):
        "新用户注册-设置密码-新建企业团队-线上微信支付"
        self.register_page.open()
        self.register_page.clear_and_sendkeys(phone_num(), self.register_page.phone_loc)
        self.register_page.send_Verification_Code()
        self.register_page.click_element(self.register_page.next_loc_btn)
        self.register_page.clear_and_sendkeys(random_name(), self.register_page.name_loc_input)
        self.register_page.clear_and_sendkeys('123456', self.register_page.pwd_loc_input)
        self.register_page.clear_and_sendkeys('123456', self.register_page.re_pwd_loc_input)
        self.register_page.click_element(self.register_page.next_loc_btn)
        self.register_page.name_send()
        self.register_page.scale_select_choice()
        self.register_page.rabdom_month_send()
        self.register_page.click_element(self.register_page.submit_loc)
        self.register_page.click_element(self.register_page.on_line_WeChat_loc)
        self.register_page.order_next_btn_click()

        self.assertEqual(self.register_page.is_page_has_text('扫码支付'), True)
        self.assertIsNotNone(self.register_page.find_element(self.register_page.zhifu_img_loc))

    def test_newuser_register_under_line(self):
        "新用户注册-设置密码-新建企业团队-线下付款并上传凭证"
        self.register_page.open()
        self.register_page.clear_and_sendkeys(phone_num(), self.register_page.phone_loc)
        self.register_page.send_Verification_Code()
        self.register_page.click_element(self.register_page.next_loc_btn)
        self.register_page.clear_and_sendkeys(random_name(), self.register_page.name_loc_input)
        self.register_page.clear_and_sendkeys('123456', self.register_page.pwd_loc_input)
        self.register_page.clear_and_sendkeys('123456', self.register_page.re_pwd_loc_input)
        self.register_page.click_element(self.register_page.next_loc_btn)
        self.register_page.name_send()
        self.register_page.scale_select_choice()
        self.register_page.rabdom_month_send()
        self.register_page.click_element(self.register_page.submit_loc)
        self.register_page.click_element(self.register_page.Under_line_loc)
        self.register_page.order_next_btn_click()
        self.register_page.wait()
        self.register_page.to_Upload_file()
        self.register_page.upload_file_input()

        self.assertEqual(self.register_page.is_page_has_text('凭证扫描图'), True)
        self.assertEqual(self.register_page.is_page_has_text('重新上传汇款凭证'), True)

    def test_old_user_register(self):
        "存在的电话号码再次注册"
        self.register_page.open()
        self.register_page.clear_and_sendkeys(random.choice(py_mysql()), self.register_page.phone_loc)
        self.register_page.send_Verification_Code()
        self.register_page.click_element(self.register_page.next_loc_btn)

        self.assertEqual(self.register_page.is_page_has_text('该手机号已存在,请前往忘记密码修改'), True)


if __name__ == '__main__':
    unittest.main()
