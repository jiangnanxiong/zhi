import unittest
from config import HTMLTestRunner

suite = unittest.TestLoader().discover("../testcase")

if __name__ == '__main__':
    # 执行用例
    # 执行测试
    # filename = config.ReportUrl + time.strftime(config.ISOTIMEFORMAT, time.localtime(time.time())) + 'result.html'
    # fp = file(filename, 'wb')
    #
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='YCG Test Report',
        description='YcgkfsApp All Testcase'
    )

    runner.run(suite)
