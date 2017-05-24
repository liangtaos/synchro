#!/usr/bin/python
#coding:utf-8

import random
import time

def sort():
    a = []
    for i in range(10):
        a.append(0)
    for i in range(5):
        nu = random.randint(0,9)
        a[nu] += 1
        print '输入数字 %s'%nu   
    for i in range(10):
        if a[i] == 0:
            print '未输入数字%s'%i
        



if __name__ == '__main__':
    sort()
