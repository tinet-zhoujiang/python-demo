#!/usr/bin/python
# -*- coding: UTF-8 -*-
# class test:
#     def hello(a):
#         print(a)
#         print(a.__class__)
# a = test()
# a.hello()
class nam:
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age=a
        self.__weight= w
    def prt(self):
        print(self.name,self.age,self.__weight)

class namm(nam):
    high=0
    def __init__(self,n,a,w,h):
        nam.__init__(self,n,a,w)
        self.high=h
    def prt(self):
        print("姓名:%s,年龄:%d,高度:%d"%(self.name,self.age,self.high))
a = namm('xc',10,130,100)
a.prt()
        
