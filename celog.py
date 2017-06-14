#!/usr/bin/python
#coding:utf-8

import logging
import log_mokai

a = '123'

if a:
    logging.error('a is a str')
else:
    print 'a is a num'
