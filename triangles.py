#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 17:01
# @Author  : Derby
# @File    : triangles.py
# 杨辉三角定义如下：打印杨辉三角
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 方法一 列表相加
def print_triangle():
    L = [1]
    while True:
        yield(L)
        L = [1] + [ L[i-1]+L[i] for i in range(1,len(L))] + [1]
func=print_triangle()
next(func)
next(func)
# 方法二：元素追加

def print_triangle1(n):
    L = [1]
    while n:
        n -= 1
        print(L)
        L = [L[i-1]+L[i] for i in range(1,len(L))]
        L.insert(0,1)
        L.append(1)



