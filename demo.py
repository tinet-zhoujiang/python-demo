#!/usr/bin/python
# -*- coding: UTF-8 -*-

# if else condition expression
# if True:
#     print("if condition is true")
# else:
#     print("if condition is fasle")
# if False:
#     print("if condition is true")
# else:
#     print("if condition is fasle")

# num = 1
# if num > 0:
#     print("a>0")
# elif num > 1:
#     print("a>1")


# while
# num = 2
# while num <= 10:
#     print("num:", num)
#     num += 1


# for
# for aaa in "asfasfgasga":
#     print(aaa)

# for list
# for aaaa in ["aaa", "bbb", "ccc"]:
#     if aaaa == "aaa":
#         print("aaaa is", aaaa)
# else:
#     print("else", aaaa)

# range
# for i in range(2,10):
#     if(i == 5):
#         continue
#     print("i",i)

# if None:
#     print("Hello")


# import sys

# a=[1,2,3,4]
# it=iter(a)
# # for i in it:
# #     print(i)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# def hello(a, b):
#     print("hello", a, b)


# hello("123", "ass")


# def changeme( mylist ):
#    mylist.append([1,2,3,4])
#    print ("函数内取值: ", mylist)
#    return

# mylist = [10,20,30]
# changeme( mylist )
# mylist[3] = "aaa"
# print ("函数外取值: ", mylist)

# sum = lambda a, b, c=1:a+b+c


# print(sum(1, 2))


# import requests
# import json
# url = 'http://www.cntour.cn/'
# strhtml = requests.get(url)
# print(strhtml.text)



# def get_translate_date(word=None):
#     url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
#     From_data={'i':word,'from':'zh-CHS','to':'en','smartresult':'dict','client':'fanyideskweb','salt':'15477056211258','sign':'b3589f32c38bc9e3876a570b8a992604','ts':'1547705621125','bv':'b33a2f3f9d09bde064c9275bcb33d94e','doctype':'json','version':'2.1','keyfrom':'fanyi.web','action':'FY_BY_REALTIME','typoResult':'false'}
#     #请求表单数据
#     response = requests.post(url,data=From_data)
#     #将Json格式字符串转字典
#     content = json.loads(response.text)
#     print(content)
#     #打印翻译后的数据
#     # print(content['translateResult'][0][0]['tgt'])
# if __name__=='__main__':
#     get_translate_date('我爱中国')

import requests
from bs4 import BeautifulSoup
import re

url='https://new.qq.com/ch/ent/'
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

strhtml=requests.get(url, headers=headers)
soup=BeautifulSoup(strhtml.text,'lxml')
data = soup.select('html')

# print(data)

for item in data:
    result={
        "title":item.get_text(),
        "link":item.get('href'),
        # 'ID':re.findall('\d+',item.get('href'))
    }
    print(result)
