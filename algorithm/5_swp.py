#!/usr/bin/python
#coding:utf-8



def maopao(li):
    for i in range(1,len(li)):
	for j in range(len(li) - i):
	    if li[j] > li[j+1]:
		tmp = li[j]
		li[j] = li[j+1]
		li[j+1] = tmp
    return li

if __name__ == '__main__':
    li = [1,110,23,32,11,14,67,45]
    print maopao(li)
