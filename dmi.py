#!/usr/bin/python
#coding:utf-8

from subprocess import Popen, PIPE
import os
import sys


def shell_cmd(cmd):
    p = Popen('%s'%cmd, shell=True,stdout=PIPE, stderr=PIPE)
    out = p.stdout.read()
    return out






if __name__ == '__main__':
    cmd = ' '.join(sys.argv[1:])
    print shell_cmd(cmd),
