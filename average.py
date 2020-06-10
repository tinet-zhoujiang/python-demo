#!/usr/bin/python
# -*- coding: UTF-8 -*-
# def main():
#     sum = 0.0
#     count = 0
#     moredata = "yes"
#     while moredata[0] == "y":
#         x = eval(input("enter a number>>"))
#         sum = sum + x
#         count = count + 1
#         moredata = input("please yes or no")
#     print("average is ", sum/count)
# main()
def main():
    sum = 0.0
    count = 0
    x = eval(input("enter a number>>"))
    while x >= 0:
        
        sum = sum + x
        count = count + 1
        x = eval(input("enter a number>>"))
    print("average is ", sum/count)
main()