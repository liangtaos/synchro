#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# @Time : 2017-10-30 16:30
# @Author : liangtao
# @File : test_file.py
import random
import codecs
numberList = [random.randint(1, 99) for i in range(20)]
numberList.sort()
nL = str(numberList)
print nL
with open('file.txt', 'w') as f:
    f.write(nL)
f = codecs.open('file.txt', 'ab+')
data = eval(f.read())
print data
data.reverse()
data = str(data)
f.seek(0, 0)
f.write('\n' + data)
f.close()
