#!/usr/bin/python
#coding:utf-8


import urllib,urllib2
import re

def getHtml(url):
    data = urllib2.urlopen(url)    
    return data.read()

def htmlRe(html):
    #li = re.findall(r'class="BDE_Image" src="(.*?)" size',html)
    li = re.findall(r'img class="BDE_Image" src=(.*?) size',html)
    print li
def main():
    url = 'http://tieba.baidu.com/p/5141114266'
    html = getHtml(url)

if __name__ == '__main__':
    main()
