#!/user/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/<name>',methods=['GET'])
def welcome(name):
    return 'welcome %s' % name

if __name__ == '__main__':
    app.run(debug=True)

# for the test how to use branch
