#!/bin/bash
#coding:utf-8

import sys
from subprocess import Popen, PIPE
from optparse import OptionParser


def opt():
    parser = OptionParser("Usage: %prog [-w WARNING] [-c CRITICAL]")
    parser.add_option('-w',
                      dest='warning',
                      action='store',
                      default='1024',
                      help='WARNING')
    parser.add_option('-c',
                      dest='critical',
                      action='store',
                      default='2048',
                      help='CRITICAL')
    options, args = parser.parse_args()
    return options, args





def getNet(wangka):
    net = Popen('ifstat -i %s 1 1'%(wangka),shell=True,stdout=PIPE)
    net = net.stdout.read().split('\n')[-2]
    input_ = net.split()[0]
    output_ = net.split()[1]
    return ( input_, output_)





def main():
    wangka = raw_input('请输入要监控的网卡 : ')
    options, args = opt()
    w = int(options.warning)
    c = int(options.critical)
    net_in, net_out = getNet(wangka)
    net_in = int(net_in)
    net_out = int(net_out)
    if net_in <  w and net_out <  w:
        print "OK",'当前进网卡流量%s kb/s, 当前出网卡流量%s kb/s'
        sys.exit(0)
    elif c >  net_in > w and c > net_out > w:
        print "WARNING", 'USED ' + str(cpu)+'%'
        sys.exit(1)
    elif w < net_in < c and w < net_out < c:
        print "CRITICAL", 'USED ' + str(cpu)+'%'
        sys.exit(2)
    else:
        print "UNKNOWN", 'USED ' + str(cpu)+'%'
        sys.exit(3)



if __name__ == '__main__':
    main()
