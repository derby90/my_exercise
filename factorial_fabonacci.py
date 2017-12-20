#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/16 16:18
# @Author  : Derby
# @File    : factorial_fabonacci.py

# 1.给定一个数字n，求n的阶乘（ 1*2*3*4...）
## 方法一：函数递归
def fact1(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
print(fact(5))

## 方法二：for循环
def fact2(n):
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    return sum

## 方法三：while循环
def fact3(n):
    sum = 1
    i = 0
    while i < n:
        i = i + 1
        sum = sum * i
    return sum


# 2.打印斐波那契数列 （0 1 1 2 3 5 8）

## 方法一：同时赋值
def fabonacci(x):
    a, b = 0, 1
    i = 0
    while i < x:
        i = i + 1
        print(b)
        a, b = b, a+b
## 方法二：