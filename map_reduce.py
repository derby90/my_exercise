#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 13:08
# @Author  : Derby
# @File    : map_reduce.py
from functools import reduce
def str_to_num(s):
    digits = {'0': 0,
              '1': 1,
              '2': 2,
              '3': 3,
              '4': 4,
              '5': 5,
              '6': 6,
              '7': 7,
              '8': 8,
              '9': 9,
              '.': -1
              }
    return digits[s]

# "456.234" => 456.234
#方法一：
def str_to_float(str_num):
    point = 0
    num = map(str_to_num,str_num)
    def to_float(f,n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10+n
        else:
            point = point*10
            return f + n/point
    return reduce(to_float,num)
print(str_to_float('4542.543'))

# 方法二
flag = 0
def to_float(f,n):
    global flag
    if n == -1:
        flag = 1
        return f
    if flag == 0:
        return f*10+n
    else:
        flag = flag *10
        return f + n/flag

#x = reduce(to_float,map(str_to_num,'45.66'))
#print(x)