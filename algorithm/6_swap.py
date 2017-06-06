#!/usr/bin/python
#coding:utf-8



def paixu(li):
    for i in range(len(li) - 1):
        for j in range(i+1,len(li)):
	    if li[i] > li[j]:
		tmp = li[i]
		li[i] = li[j]
		li[j] = tmp
    return li

print paixu([2,3,4,1,118,3,9])
