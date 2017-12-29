#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 19:29
# @Author  : Derby
# @File    : hanoi.py

# >>>move(3, 'A', 'B', 'C')
# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
def movie(n,a,b,c):
    if n == 1:
        print('movie',a, '-->', c)
    else:
        movie(n-1,a,c,b)
        movie(1,a,b,c)
        movie(n-1,b,a,c)


