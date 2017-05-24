#!/usr/bin/python
#coding:utf-8
import random
import time
def main():
    a = []
    a_sort = []
    for i in xrange(10000000):
        a.append(0)
    for i in xrange(1000000):
        nu = random.randint(0,100000)
        #print '输入数字%s'%(nu)
        a[nu] += 1
    for i in xrange(len(a)):
        for j in range(a[i]):
	    a_sort.append(i)
    return a_sort






if __name__ == '__main__':
    start = time.time()   
    a_sort = main()
    
    #print '排序后的数字', a_sort
    end = time.time()
    print end -start
