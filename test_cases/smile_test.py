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
        create_task_res = self.create_task("test", "desc")
        create_task_id = create_task_res["id"]
        url = self.ip + "/" + str(create_task_id)
        response = requests.request("GET", url)
        res = response.json()
        print (res)
        self.assertEqual(res["title"], "test")
        self.assertEqual(res["desc"], "desc")
        requests.request("DELETE", url)

    def test_put_task(self):
        """"完成一个任务"""
        create_task_res = self.create_task("test", "desc")
        create_task_id = create_task_res["id"]
        url = self.ip + "/" + str(create_task_id)
        response = requests.request("PUT", url)
        res = response.json()
        print (res)
        self.assertEqual(res["id"], create_task_id)
        self.assertEqual(res["done"], True)
        requests.request("DELETE", url)

    def test_post_task(self):
        """"创建一个任务"""
        create_task_res = self.create_task("test", "desc")
        create_task_id = create_task_res["id"]
        url = self.ip + "/" + str(create_task_id)
        print (create_task_res)
        self.assertEqual(create_task_res["title"], "test")
        self.assertEqual(create_task_res["desc"], "desc")
        requests.request("DELETE", url)
    def test_delete_task(self):
        """"删除一个任务"""
        create_task_res = self.create_task("test", "desc")
        create_task_id = create_task_res["id"]
        url = self.ip + "/" + str(create_task_id)
        response = requests.request("DELETE", url)
        res = response.json()
        print (res)
        self.assertEqual(res["id"], str(create_task_id))

    def create_task(self, title, desc):
        url = self.ip
        payload = json.dumps({'title': title, 'desc': desc})
       # payload1 = {'title': title, 'desc': desc}
        headers = {'content-type': "application/json"}
        response = requests.request("POST", url, data=payload, headers=headers)
        return response.json()


if __name__ == '__main__':
    #unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(SmileTaskTestCase('test_delete_task'))
    runner = unittest.TextTestRunner()
    runner.run(suit)