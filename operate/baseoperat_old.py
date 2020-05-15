from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from config.sysconfig import *
from selenium.webdriver.support import expected_conditions as EC

import sys
import time


# 基础操作
class BaseOperate():
    # 声明一个webdriver类
    operate_driver = webdriver.Chrome

    def __init__(self, driver):
        # 构造函数里将driver传入
        self.operate_driver = driver

    def find_element(self, *loc):
        """
        重封装的find方法，接受元祖类型的参数，默认等待元素5秒，寻找失败时自动截图
        :param loc:元组类型,必须是(By.NAME, 'username')这样的结构
        :return:元素对象webelement
        """
        try:
            webelement = WebDriverWait(self.operate_driver, 10).until(lambda x: x.find_element(*loc))
            return webelement
        except (TimeoutException, NoSuchElementException) as e:
            # 寻找失败时自动截图至指定目录sreenshot，截图名称为调用方法名（测试用例名）+ 时间戳 + png后缀
            self.operate_driver.get_screenshot_as_file(
                SCREENSHOTURL + sys._getframe(1).f_code.co_name + time.strftime(ISOTIMEFORMAT,
                                                                                time.localtime(time.time())) + ".png")

    def find_element2(self, *loc):

        try:
            webelement = WebDriverWait(self.operate_driver, 10).until(EC.presence_of_all_elements_located(*loc),message="")
            print(webelement)
            return webelement
        except (TimeoutException, NoSuchElementException) as e:
            # 寻找失败时自动截图至指定目录sreenshot，截图名称为调用方法名（测试用例名）+ 时间戳 + png后缀
            self.operate_driver.get_screenshot_as_file(
                SCREENSHOTURL + sys._getframe(1).f_code.co_name + time.strftime(ISOTIMEFORMAT,
                                                                                time.localtime(time.time())) + ".png")

    def click_element(self, *loc):
        """
        重封装的click方法，将寻找和点击封装到一起，适用于点击次数不多的元素
        :param loc:元组类型,必须是(By.NAME, 'username')这样的结构
        :return:None
        """
        try:
            webelement = self.find_element2(*loc)
            webelement.click()
        except (TimeoutException, NoSuchElementException) as e:
            print('Error details :%s' % (e.msg))

    def is_page_has_text(self, text):
        """
        判断当前页面是否存在指定的文字
        :param text:字符串类型，要判断是否存在的文字
        :return:布尔值，True代表存在，False代表不存在
        """
        nowtime = time.time()
        while self.operate_driver.page_source.find(text) < 0:
            time.sleep(2)
            if time.time() - nowtime >= 30000:
                return False
        return True

    def switch_to_last_handles(self):
        """
        在打开的窗口里选择最后一个
        :return:None
        """
        all_handles = self.operate_driver.window_handles
        self.operate_driver.switch_to_window(all_handles[-1])

    def switch_to_another_hanles(self, now_handle):
        """
        只适用于打开两个窗口的情况，传入现在的窗口句柄后，选择另一个窗口
        :param now_handle:现在的窗口句柄
        :return:
        """
        # 得到当前开启的所有窗口的句柄
        all_handles = self.operate_driver.window_handles
        # 获取到与当前窗口不一样的窗口
        for handle in all_handles:
            if handle != now_handle:
                self.operate_driver.switch_to_window(handle)

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
            print('Error details :%s' % (e.msg))
