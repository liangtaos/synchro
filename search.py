#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get99num():
    list_num = []
    while 1:
        if len(list_num) == 9:break
        nu = random.randint(1,10)
        if nu not in list_num:list_num.append(nu)
    return list_num

def getNu(list_num):
    for i in range(1,11):
        if i in list_num:
            continue
        else:
            out = i
        
    return out

if __name__ == '__main__':
    list_num = get99num()
    print list_num
    print getNu(list_num)

