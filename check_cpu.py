#!/usr/bin/env python

import sys
from optparse import OptionParser

def opt():
    parser = OptionParser("Usage: %prog [-w WARNING] [-c CRITICAL]")
    parser.add_option('-w',
                      dest='warning',
                      action='store',
                      default='80',
                      help='WARNING')
    parser.add_option('-c',
                      dest='critical',
                      action='store',
                      default='90',
                      help='CRITICAL')
    options, args = parser.parse_args()
    return options, args

def processCpu(line):
    lines = line.split()
    cpuinfo = ('%.2f'%(float(int(lines[1]) + int(lines[2]) + int(lines[3])) / float(int(lines[1]) + int(lines[2]) + int(lines[3]) + int(lines[4])) * 100))
    return cpuinfo


def getCpu(f):
    with open(f) as fd:
        for line in fd:
            if line.split()[0] == 'cpu':
                allcpu = processCpu(line)
                break
    return allcpu 

def main():
    options, args = opt()
    w = int(options.warning)
    c = int(options.critical)
    cpu = getCpu('/proc/stat')
    if cpu > w:
        print "OK",'used ' + str(cpu)+'%'
        sys.exit(0)
    elif c < cpu <= w:
        print "WARNING", 'used ' + str(cpu)+'%'
        sys.exit(1)
    elif cpu < c:
        print "CRITICAL", 'used ' + str(cpu)+'%'
        sys.exit(2)
    else:
        print "UNKNOWN", 'used ' + str(cpu)+'%'
        sys.exit(3)

if __name__ == '__main__':
    main()
