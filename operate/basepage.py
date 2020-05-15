from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from config.sysconfig import *
from selenium.webdriver.support import expected_conditions as EC
import sys
import time


class BasePage(object):
    """
    BasePage封装所有页面都公用的方法，例如driver, url ,FindElement等
    """

    # 初始化driver、url、pagetitle等
    # 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参。
    # __init__方法不能有返回值，只能返回None
    # self只实例本身，相较于类Page而言。
    def __init__(self, selenium_driver):
        self.driver = selenium_driver

    def _open(self, url):
        self.driver.get(url)

    def find_element(self, loc):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc))
            return element
        except (TimeoutException, NoSuchElementException) as e:
            self.driver.get_screenshot_as_file(
                SCREENSHOTURL + sys._getframe(1).f_code.co_name + time.strftime(ISOTIMEFORMAT,
                                                                                time.localtime(time.time())) + ".png")

    def click_element(self, loc):
        try:
            element = self.find_element(loc)
            element.click()
        except (TimeoutException, NoSuchElementException) as e:
            print('Error details :{}'.format(e.msg))

    def is_page_has_text(self, text):
        """
        判断当前页面是否存在指定的文字
        :param text:字符串类型，要判断是否存在的文字
        :return:布尔值，True代表存在，False代表不存在
        """
        nowtime = time.time()
        while self.driver.page_source.find(text) < 0:
            time.sleep(2)
            if time.time() - nowtime >= 5:
                return False
        return True

    def switch_to_last_handles(self):
        """
        在打开的窗口里选择最后一个
        :return:None
        """
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])

    def switch_to_another_hanles(self, now_handle):
        """
        只适用于打开两个窗口的情况，传入现在的窗口句柄后，选择另一个窗口
        :param now_handle:现在的窗口句柄
        :return:
        """
        # 得到当前开启的所有窗口的句柄
        all_handles = self.driver.window_handles
        # 获取到与当前窗口不一样的窗口
        for handle in all_handles:
            if handle != now_handle:
                self.driver.switch_to_window(handle)

    def clear_and_sendkeys(self, sendtexts, *loc):
        """
        先清除当前文本框内的文字再输入新的文字的方法
        :param sendtexts:要输入的新的文字
        :param loc:元组类型,必须是(By.NAME, 'username')这样的结构
        :return:None
        """
        try:
            webelement = self.find_element(*loc)
            webelement.clear()
            webelement.send_keys(sendtexts)
        except (TimeoutException, NoSuchElementException) as e:
            print('Error details :{}'.format(e.msg))

    def input_sendkeys(self, sendtexts, *loc):

        try:
            webelement = self.find_element(*loc)
            webelement.send_keys(sendtexts)
        except (TimeoutException, NoSuchElementException) as e:
            print('Error details :{}'.format(e.msg))

    def wait(self, times=1):
        time.sleep(times)

    def focus_element(self, *loc):
        try:
            target = self.find_element(*loc)  # 要聚焦的目标元素
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
        except (TimeoutException, NoSuchElementException) as e:
            print('Error details :{}'.format(e.msg))
