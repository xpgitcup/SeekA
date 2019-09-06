# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    # target = 'http://www.biqukan.com/1_1094/5403177.html'
    url="https://www.biqutxt.com/70_70220/22917987.html"
    req = requests.get(url)
    print(req.text)
