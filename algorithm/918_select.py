#!/usr/bin/python
#coding:utf-8





def main(li=[]):
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if li[i] > li[j]:
	        swap = li[i]
		li[i] = li[j]
                li[j] = swap 
    return li







if __name__ == '__main__':
    li = []
    import random
    for i in range(0,1000):
        li.append(random.randint(0,9999))
    print main(li)
