#!/usr/bin/python
#coding:utf-8

import random
import time

def maopao(li):
    for j in range(1,len(li)-1):
        for i in range(len(li) - j):
            if li[i] > li[i + 1]:
	        tmp = li[i]
                li[i] = li[i + 1]
                li[i+1] = tmp
    return li

if __name__ == '__main__':
    li = [random.randint(0,999999) for i in xrange(1000000)]
    start = time.time()
    print maopao(li)
    print time.time() - start

    
    
