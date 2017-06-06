#!/usr/bin/python
#coding:utf-8



import random
import time
def main(li):
    for i in range(len(li) -1):
        min_ = i
        for j in range(i+1, len(li)):
            if li[min_] > li[j]:
                #tmp = li[i]
                #li[i] = li[j]
                #li[j] = tmp
                min_ = j
        tmp = li[i]
        li[i] = li[min_]
        li[min_] = tmp
    return li

if __name__ == '__main__':
    start = time.time()
    li = [ random.randint(0,9999) for i in xrange(100000)]
    #print '*' * 60
    print main(li)
    print time.time() - start

