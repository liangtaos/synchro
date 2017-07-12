#/usr/bin/env python
# coding:utf-8

import os
import sys



def listDir(dir):
    sum = 0
    for d,f,i in os.walk(dir):
        #print d, f, i
        #print os.path.join(d,i)
        for files in i:
	    #if os.path.isfile(os.path.join(d,files)):
	    print os.path.join(d,files)
	    sum += 1
    print '%s下面总共有%d个文件'%(dir, sum)

def main():
    dir = sys.argv[1]
    listDir(dir)

if __name__ == '__main__':
    main()
