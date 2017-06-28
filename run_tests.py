import unittest
from HTMLTestRunner import HTMLTestRunner
import time
test_dir = "./test_cases"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py',top_level_dir=None)
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title="restful test report", description="wwww")
    runner.run(discover)
    fp.close()