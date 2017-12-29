#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/27 12:24
# @Author  : Derby
# @File    : decorater.py
import datetime
import random
import functools

# 不带参数的装饰器
def time_log(func):
    def innter(*args,**kwargs):
        print(datetime.datetime.now().strftime('%Y-%m-%d'))
        return func(*args,**kwargs)
    return innter

@time_log
def num_random(n):
    for i in range(1,n):
        print(random.randrange(0,45))

#带参数的装饰器
def call_log(*text):
    def innter(func):
        @functools.wraps(func) # 保证函数变量func的名字不被更改
        def wraper(*args,**kwargs):
            print('%s Begin Call:%s' % (text[0], func.__name__))
            func(*args,**kwargs)
            print('%s End Call:%s' % (text[0], func.__name__))
        return wraper
    return innter

@call_log()
def manifasto():
    print('大王叫我来巡山')

manifasto()
