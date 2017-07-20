"""
from flask import Flask
app = Flask(__name__)

def hello():
    return "Hello World!"
"""
from flask import Flask
app = Flask(__name__)

@app.route("/") # 路由
def hello(): # handler
    return "Hello World!"