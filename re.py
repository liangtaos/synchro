#!/usr/bin/python
#coding:utf-8


import re
import sys
from subprocess import Popen, PIPE


def process_cmd(cmd):
    p = Popen('%s'%cmd,shell=True,stdout=PIPE,stderr=PIPE)
    data = p.stdout.read()
    if data:
	return data
    else:
	return None



def get_info(data):
    out = {}
    pattern = re.compile(r'\w{2,3}\d .*? Link encap:Ethernet  HWaddr [\w+:]{5,17}.*?[\s].*?inet addr:[\d\.]{7,15}.*?[\s]')
    info = re.findall(pattern, data)
    for li in info:
        name = li.split()[0]
        mac = li.split()[4]
        ip = li.split()[6].split(':')[1]
        out[name] = [mac, ip]
    return out
def main():
    cmd = sys.argv[1]
    data = process_cmd(cmd)
    if not data:
	print 'cmd error'
    else:
	print get_info(data)
	
    





if __name__ == '__main__':
    main()
