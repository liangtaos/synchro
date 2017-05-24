#!/usr/bin/python
#coding:utf-8

def swap(x, y ):
    c = x
    x = y
    y = c
    return x ,y


if __name__ == '__main__':
    x = raw_input('Plese input a nu x: ')
    y = raw_input('Plese input a nu y: ')
    print '输入的数字是x: %s, y: %s'%(x,y)
    x, y = swap(x, y)
    print '输出的数字是x: %s, y: %s'%(x,y)
    print __name__
    print __file__
