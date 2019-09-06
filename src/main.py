import urllib.request
import socket
import urllib.error
from urllib import request, parse

# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

# response = urllib.request.urlopen('https://www.python.org')
# print(type(response))

# response = urllib.request.urlopen('https://www.python.org')
# print(type(response))

# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# 给请求添加头部信息
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'zhaofan'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# from urllib import request, parse
#
# url = 'http://httpbin.org/post'
# dict = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# import re
#
# html = '''<div id="songs-list">
#     <h2 class="title">经典老歌</h2>
#     <p class="introduction">
#         经典老歌列表
#     </p>
#     <ul id="list" class="list-group">
#         <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦">往事随风</a>
#         </li>
#         <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
#         <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
#         <li data-view="5">
#             <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
#         </li>
#     </ul>
# </div>'''
#
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
# print(result)
# print(result.groups())
# print(result.group(1))
# print(result.group(2))

# import requests
# import json
#
# requests.post("http://httpbin.org/post")
# requests.put("http://httpbin.org/put")
# requests.delete("http://httpbin.org/delete")
# requests.head("http://httpbin.org/get")
# requests.options("http://httpbin.org/get")


# response = requests.get("http://httpbin.org/get")
# print(type(response.text))
# print(response.json())
# print(json.loads(response.text))
# print(type(response.json()))
#
# import requests
#
# response = requests.get("http://www.baidu.com")
# print(response.cookies)
#
# for key,value in response.cookies.items():
#     print(key+"="+value)

# from bs4 import BeautifulSoup
#
# html = '''
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# '''
# soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p["class"])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id='link3'))


import requests
import re
content = requests.get('https://book.douban.com/').text
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)
print(results)

for result in results:
    url,name,author,date = result
    author = re.sub('\s','',author)
    date = re.sub('\s','',date)
    print(url,name,author,date)