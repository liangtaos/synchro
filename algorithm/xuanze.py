#!/usr/local/python
#coding:utf-8


def ze(li):
    for i in range(1, len(li)):
	for j in xrange(len(li) - i):
	    if li[j] > li[j+1]:
		tmp = li[j]
	        li[j] = li[j+1]
                li[j+1] = tmp
    return li

if __name__ == '__main__':
    import random
    li = []
    for i in xrange(20):
	n = random.randint(0,100)
        li.append(n)
    print '未排序的: ',li
    print '排序的: ', ze(li)
