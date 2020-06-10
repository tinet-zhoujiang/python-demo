#!/usr/bin/python
# -*- coding: UTF-8 -*-
# day = "星期一星期二星期三星期四星期五星期六星期天"
# n = input("请输入天数(1-7):")
# m = (int(n)-1)*3
# dayadd = day[m:m+3]
# print("中文结果是"+dayadd)

# s = "abcd1234"
# a = s.find('cd')
# print (a)


# val = pow(2,1000)
# v = len(str(val))
# print (v)

# for i in range(5):
#     print("*"*(i+1))
# print(5*"1")

# sum = 0
# number = 0
# while number  < 5 :
#     number = number +1  1   2   3
#     sum += number        1   3  6
#     if sum>5:
#         break
# print("the number is" ,number)
# print("sum is " ,sum)

for num in range(2,10):
    for x in range(2,num):
        print(x,num)
        continue
    else:
        print('heel')
    