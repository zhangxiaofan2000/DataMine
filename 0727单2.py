# Python爬取豆瓣影评
#(爬取其他电影影评需替换'User-Agent'和打印网址)

import requests
from bs4 import BeautifulSoup

# 自定义根据每页影评的url爬取影评的方法
def getData(url):

 # 请求头为字典格式（可自定义替换'User-Agent'）
 headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
 }

 # 携带请求头去发请求
 response = requests.get(url=url, headers=headers)

 # 使用bs4和html5lib解析网页内容
 bs = BeautifulSoup(response.content, 'html5lib')

 # 获取所有的评论  span标签
 short_list = bs.find_all("span", attrs={"class": "short"})

 # 遍历shortList
 for short in short_list:
     # 获取标签内部的文字
     content = short.text
     print(content)


# main函数：整个程序的入口
if __name__ == '__main__':
 for i in range(1):  # 打印的次数
     # 可自定义替换地址
     baseurl = 'https://movie.douban.com/subject/30174085/comments?sort=new_score&status=P'
     baseurl = baseurl.format(i * 20)  # 打印的范围（条数）
     # 循环调用爬取每页影评的方法
     getData(baseurl)