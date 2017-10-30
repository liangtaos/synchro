#!/usr/bin/env python
#coding:utf-8


def main(li=[]):
    for i in xrange(1, len(li)):
        for j in xrange(len(li) - i):
	    if li[j] > li[j+1]:
		swp = li[j]
                li[j] = li[j+1]
                li[j+1] =swp
    return li





if __name__ == '__main__':
    import random
    li = []
    for i in range(20):
        li.append(random.randint(0,100))
    print '未排序的：%s'%(li)
    print '已排序的：',main(li)
