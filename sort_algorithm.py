#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/22 11:26
# @Author  : Derby
# @File    : sort_algorithm.py
# Python 实现八大排序算法

# 生成一组随机数
import random
## 方法一 循环
def generation_num(num,num_range):
    L = []
    while num:
        L.append(random.randint(0,num_range))
        num -= 1
    return L
##方法二 列表生成式
L = [random.randrange(1000) for i in range(100)] #从1000的范围随机选100个数
L1 = random.sample([i for i in range(100)],20)   #从100 个数的列表里，选取20个不重复的随机数


## 插入排序--直接插入排序（Straight insertion sort）
def sort1(L):
    num = len(L)
    for x in range(1,num):
        key = L[x]
        j = x - 1
        while j >= 0:
            if  L[j] > key:
                L[j+1] = L[j]
                L[j] = key
            j -= 1
    return L
## 插入排序--希尔排序（Shell sort）





