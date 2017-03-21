#!/usr/bin/python
#coding:utf-8

import hashlib
import sys
import os

def md5sum(f):
    md5 = hashlib.md5()
    fd = open(f)
    while 1:
        data = fd.read(1024 * 4)
	if data:
            md5.update(data)
        else:
	    break
    fd.close()
    return md5.hexdigest()

def bianli(dir):
    file_all = []
    for d, p, f in os.walk(dir):
        for fi in f:
            file_name = os.path.join(d,fi)
	    file_all.append(file_name)
    return file_all


def md5sum_dir(dir):
    f_list = bianli(dir)
    with open('/root/.md5', 'w') as f:
        for fd in f_list:
            try:
	        md5_sum = md5sum(fd)
	        f.write(md5_sum)
            except:
		print 'not read'
		continue
    md5_dir = md5sum('/root/.md5')
    return md5_dir


if __name__ == '__main__':
    input_ = sys.argv[1].strip()
    if os.path.isdir(input_):
        print md5sum_dir(input_)
    elif os.path.isfile(input_):
	print md5sum(input_)
    else:
	print 'you should input right dir or file'
