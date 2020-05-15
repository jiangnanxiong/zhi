import unittest

suite = unittest.TestSuite(unittest.makeSuite("你的测试用例类名"))

if __name__ == '__main__':
    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)