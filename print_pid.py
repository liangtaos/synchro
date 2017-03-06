#!/usr/bin/env python
# coding=utf-8

import os

def main():
    pidall = []
    nu_all = os.listdir('/proc/')
    for nu in nu_all:
        try:
            nu = int(nu)
            pidall.append(nu)
        except:
            continue
    return pidall



if __name__ == '__main__':
    print main()
    
