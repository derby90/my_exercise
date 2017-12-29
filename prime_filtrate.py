#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 14:55
# @Author  : Derby
# @File    : prime_filtrate.py

# 使用fileter 埃拉托色尼筛选法 筛选素数
# # definition greater then 3 prime number
# def num_generation():
#     n = 1
#     while True:
#         n += 2
#         yield n
#
# def prime_fileter(num):
#     return lambda x: x % num > 0
#
# def prime_generation():
#     yield 2
#     it = num_generation()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(prime_fileter(n),it)
#
#
# for n in prime_generation():
#     if n < 1000:
#         print (n)
#     else:
#         break

# 使用fileter 筛选回数 如 123321,909
def num_generation1():
    n = 10
    while True:
        n += 1
        yield n

def filter_num(num):
    return lambda num: num == int(str(num)[::-1])
    #if str(num) == str(num)[::-1]:  # 更简单的方法  return num == int(str(num)[::-1])
     #   return num

def gen_palindrome():
    it = num_generation1()
    while True:
        num = next(it)
        yield num
        it = filter(filter_num(num),it)

for i in gen_palindrome():
    if i < 1000:
        print(i)
    else:
        break
