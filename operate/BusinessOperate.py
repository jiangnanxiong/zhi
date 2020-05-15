from maincase.loginpage import LoginPage


# 基础业务逻辑
class Login_Public(LoginPage):

    def start_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        # 调用打开页面组件
        login_page.click_login_btn()
        login_page.click_username_input()
        login_page.click_password_input()
        login_page.click_submit_btn()
        login_page.click_queding_loc_btn()
        login_page.wait()
