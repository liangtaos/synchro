#!/usr/local/python
#coding:utf-8

import random
import sys


def pao(li):
    for i in range(len(li)):
	for j in range(i+1, len(li)):
	    if li[i] > li[j]:
		tmp = li[i]
		li[i] = li[j]
		li[j] = tmp
    return li





if __name__ == '__main__':
    li = []
    for i in xrange(100):
	n = random.randint(1,100)
        if n in li:continue
    	li.append(n)
    print '未排序的: ',li,len(li)
    n_li = pao(li)
    print '已排序的: ',n_li,len(n_li)
