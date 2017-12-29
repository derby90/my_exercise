#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/22 10:38
# @Author  : Derby
# @File    : find_number.py

# 找一个列表中的最大值，和最小值并且返回一个tuple
L = [4,8,3,8,9,0,242,5,74,3,3,5,6,7,8]
print(L)
def find_max_and_mix():
    for i in range(len(L)-1):
        for i in range(len(L)-1):
            if L[i] >= L[i+1]:
                L[i],L[i+1] = L[i+1],L[i]
    print(L)
find_max_and_mix()