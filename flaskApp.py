# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 10:10:38 2019

@author: Jasdeep
"""

from flask import Flask
app= Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__' :
    app.run()