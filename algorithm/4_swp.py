#!/usr/bin/python
#coding:utf-8



import random
import time
def main(li):
    for i in range(len(li) -1):
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
		tmp = li[i]
                li[i] = li[j]
		li[j] = tmp
    return li

if __name__ == '__main__':
    li = [ random.randint(0,99999) for i in xrange(1000000)]
    #print '*' * 60
    print main(li)
