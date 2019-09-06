# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html, features="lxml")
    texts = bf.find_all('div', id='content')
    print(texts)
