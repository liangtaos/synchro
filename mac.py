#!/usr/bin/env python
# -*- coding: utf-8 -*-

import readline

def getNextMac(mac):
    new_last_two = int(mac, 16) + 1
    new_last_two = hex(new_last_two)[2:]
    if len(new_last_two) < 2:
        new_last_two = '0' + str(new_last_two)
    return new_last_two

def main():
    mac = raw_input('input mac :')
    base_mac = mac[:-3]
    last_two = mac[-2:]
    if last_two == 'FF':
        last_two2 = base_mac[:-3]
        last_two2_2 = base_mac[-2:]
        last_four = getNextMac(last_two2_2)
        new_mac = last_two2 + ':' + last_four.upper() + ':' + '00'
        print 'NEXT MAC is %s'%(new_mac)
    else:
        new_last_two = getNextMac(last_two)
        new_mac = base_mac + ':' + new_last_two.upper()
        print 'NEXT MAC is %s'%(new_mac)

if __name__ == '__main__':
    main()
