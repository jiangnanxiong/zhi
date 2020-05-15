import unittest
import os
from config.HTMLTestRunner import HTMLTestRunner
from datetime import datetime
from util.email_test import *
import time

cases = unittest.defaultTestLoader.discover("../testcase", pattern='test_login.py')

if __name__ == '__main__':
    with open('./testreport/report-{}.html'.format(datetime.now().strftime('%Y%m%d%H%M')), 'w',
              encoding='utf8') as f:
        runner = HTMLTestRunner(stream=f, title='智训测试报告', description='测试案例')
        runner.run(cases)

    # send_mail(file_report())
