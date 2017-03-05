#!/usr/bin/env python
# coding=utf-8


import random

def getRandom():
    return random.randint(1,10)


def main():
    number = getRandom()
    count = 1
    while 1:
        if count > 4: 
            print 'times over '
            break
        nu = int(raw_input('Please input a number which follow you heart :'))
        if nu == number:
            print 'you right'
            break
        elif nu > number:
            print 'too big next input'
            count += 1
        elif nu < number:
            print 'too small next input'
            count += 1

if __name__ == '__main__':
    main()
