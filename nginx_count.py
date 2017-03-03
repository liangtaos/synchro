#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os  


def getPid(server):
    pid_nu = os.popen('pidof %s'%(server)).read().strip()
    return pid_nu

def getMem(nu):
    with open('/proc/%s/status'%(nu)) as f:
        for line in f.readlines():
            if line.startswith('VmRSS'):
                mem_ = int(line.split()[1])
                print mem_
                break
    return mem_

def getSysMem():
    with open('/proc/meminfo') as f:
        for line in f:
            if line.startswith('MemTotal'):
                mem_all = int(line.split()[1])
                break
    return mem_all


def main():
    server = raw_input('please input you server : ')
    pid_nu = getPid(server)
    all_server = 0
    for nu in pid_nu.split():
        mem = getMem(nu)
        all_server += mem
    mem_sys = getSysMem()
    print all_server,mem_sys
    v =(float(all_server) / float(mem_sys)) * 100 
    v = str('%.2f'%(v)) + '%'
    print v
    all_server_mem = str('%.2f'%(all_server / 1000.0)) + 'M'
    print '%s 占用内存 %s'%(server, all_server_mem)
    print '%s 占用的百分比 %s'%(server, v)







if __name__ == '__main__':
    main()
