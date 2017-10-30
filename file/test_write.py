#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# @Time : 2017-10-30 17:17
# @Author : liangtao
# @File : test_write.py
import json
string = 'my name is allen , i love python'
list_ = ['my', 'name', 'is', 'allen', 'i', 'love', 'python']
tuple_ = ('my', 'name', 'is', 'allen', 'i', 'love', 'python')
dict_ = {'name': 'allen', 'interest': 'python'}
with open('file', 'ab+') as f:
    f.write(string + '\n')
    f.write(str(list_) + '\n')
    f.write(str(tuple_) + '\n')
    f.write(json.dumps(dict_) + '\n')

print 'over'