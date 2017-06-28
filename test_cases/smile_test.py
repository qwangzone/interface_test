import unittest
import requests
import json
import time
from parameterized import parameterized
class SmileTaskTestCase(unittest.TestCase):
    def setUp(self):
        self.ip = 'http://localhost:3000/api/tasks'

    def test_get_all_tasks(self):
        """获取所有任务"""
        url = self.ip
        response = requests.request("GET", url)
        res = response.json()
        print (res)
        self.assertNotEqual(res, [])

    def test_get_task(self):
        """获取单个任务的详情"""
        url = self.ip + "/1"
        response = requests.request("GET", url)
        res = response.json()
        print (res)
        self.assertEqual(res["title"], "test1")
        self.assertEqual(res["desc"], "test1")

    def test_put_task(self):
        """"完成一个任务"""
        url = self.ip + "/2"
        response = requests.request("PUT", url)
        res = response.json()
        print (res)
        self.assertEqual(res["done"], True)

    def test_post_task(self):
        """"创建一个任务"""
        payload = {"title": "wq", "desc": "wq"}
        response = requests.post(self.ip,data=payload)
        res = response.json()
        print (res)
        self.assertEqual(res["title"], "wq")
        self.assertEqual(res["desc"], "wq")

    def test_delete_task(self):
        """"删除一个任务"""
        url = self.ip + "/6"
        response = requests.request("DELETE", url)
        res = response.json()
        print (res)
        self.assertEqual(res["id"], '6')


if __name__ == '__main__':
    unittest.main()
    #suit = unittest.TestSuite()
    #suit.addTest(SmileTaskTestCase('test_delete_task'))
    #runner = unittest.TextTestRunner()
    #runner.run(suit)