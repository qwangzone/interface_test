import unittest
import json
import requests
class SmileTaskTestCase(unittest.TestCase):
    def setUp(self):
        self.ip = 'http://127.0.0.1:3000'
        self.token = self.login('admin', 'admin')
    """
   #注册用户
    def register(self, username, password, password_confirmation):
        url = self.ip + "/register"
        response = requests.request("POST", url, data={"username": username, "password": password, "password_confirmation" : password_confirmation})
        res = response.json()
        print (res)
    """
    def login(self, username, password):
        #self.register("admin", "admin", "admin")
        url = self.ip + "/login"
        res = requests.request("POST", url, data={'username': username, 'password': password}).json()
        print(res)
        return res['token']

    @property
    def headers_with_jwt(self):
        return {'Authorization': 'Bearer ' + self.token, 'content-type': 'application/json'}

    def create_task(self, title, desc):
        url = self.ip + "/api/tasks"
        payload =json.dumps({'title': title, 'desc': desc})
        response = requests.request("POST", url, data=payload, headers=self.headers_with_jwt)
        return response.json()

    def test_create_task(self):
        res = self.create_task('wq', 'wangqi')
        print (res)
        self.assertEqual(res['title'], 'wq')

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(SmileTaskTestCase('test_create_task'))
    runner = unittest.TextTestRunner()
    runner.run(suit)