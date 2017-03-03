#!/usr/bin/env python
# -*- coding: utf-8 -*-
import readline


def shi2er(nu):
    a = []
    while 1:
        yu = nu % 2
        a.append(yu)
        nu = nu / 2 
        if nu < 2:
            a.append(1)
            break
    b = a[::-1]
    c = ''.join([str(a) for a in b])
    lens = len(c)
    if lens < 8 : c = '0' * (8 - len(c)) + c
    if 16 > lens > 8 : c = '0' * (16 - len(c)) +c
    if lens > 16: c = c 
    return c

def er2shi(nu):
    numb = 0
    nu_str = str(nu)
    nu_str = nu_str[::-1]
    lens = len(nu_str)
    for i in range(lens):
        if nu_str[i] == '1':
            numb = numb + 2 ** i
    return numb
            


if __name__ == '__main__':
    x = int(raw_input('please input decimal number: '))
    out2 = shi2er(x)
    print out2
    y = int(raw_input('please input binary number : '))
    out10 = er2shi(y)
    print out10

