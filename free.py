#!/usr/bin/env python
# -*- coding: utf-8 -*-



def getFree():
    out = {}
    with open('/proc/meminfo') as f:
        for line in f.readlines():
            if line.startswith('MemTotal'):
                mem_total = int(line.split()[1])
            elif line.startswith('MemFree'):
                mem_free = int(line.split()[1])
            elif line.startswith('Buffers'):
                buffers = int(line.split()[1])
            elif line.startswith('Cached'):
                cached = int(line.split()[1])
            else:
                continue
    free_ = str('%.2f'%((float(mem_free + buffers + cached) / float(mem_total)) * 100)) + '%'
    out['free_odd'] = free_
    return out


def processCpu(line):
    lines = line.split()
    cpuinfo = str('%.2f'%(float(int(lines[1]) + int(lines[2]) + int(lines[3])) / float(int(lines[1]) + int(lines[2]) + int(lines[3]) + int(lines[4])) * 100)) + '%'
    return cpuinfo
    

def getCpu():
    out = {}
    with open('/proc/stat') as f:
        for line in f.readlines():
            if line.split()[0] == 'cpu':
                allcpu = processCpu(line)
                out['cpuall_used'] = allcpu
                continue
            elif line.startswith('cpu'):
                dev = line.split()[0]
                cpuinfo = processCpu(line)
                out['%s_used'%dev] = cpuinfo
    return out


def main():
    free_ = getFree()
    print free_
    cpu_ = getCpu()
    print cpu_


if __name__ == '__main__':
    main()
