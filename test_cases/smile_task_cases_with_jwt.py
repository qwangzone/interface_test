import unittest
import json
import requests
class SmileTaskTestCase(unittest.TestCase):
    def setUp(self):
        self.ip = 'http://127.0.0.1:3000'
        self.token = self.login('admin', 'admin')

    def login(self, username, password):
        url = self.ip + "/login"
        res = requests.request("POST", url, data={'username': username, 'password': password}).json()
        print(res)
        return res['token']

    @property
    def headers_with_jwt(self):
        return {'Authrization': 'Bearer' + self.token, 'content-type': 'application/json'}

    def create_task(self, title, desc):
        url = self.ip + "/api/tasks"
        payload =json.dumps({'title': title, 'desc': desc})
        response = requests.request("POST", url, headers=self.headers_with_jwt)
        return response.json()

    def test_create_task(self):
        res = self.create_task('wq', 'wangqi')
        self.assertEqual(res['title'], 'wq')
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(SmileTaskTestCase('test_create_task'))
    runner = unittest.TextTestRunner()
    runner.run(suit)