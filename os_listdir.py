#!/usr/bin/env python
# coding=utf-8

import os
import sys


def getFile(path):
    print os.listdir(path)
    print '*' * 30
    for f in os.listdir(path):
        if os.path.isfile(f):
            print f
        else:
            f_new = os.path.join(path,f)
            print f_new
            getFile(f_new)





def main():
    fd = sys.argv[1] 
    getFile(fd)





if __name__ == '__main__':
    main()
