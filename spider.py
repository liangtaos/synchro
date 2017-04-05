#!/usr/bin/python
#coding:utf-8

import requests
import re
def get_page():
    urls=['http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&pn={}&gsm=3c00000000003c'.format(num) for num in range(0,20000,20)]
    for url in urls:
        print url
        try:
            get_img_link(url)
        except:
            continue

def get_img_link(url):
    r=requests.get(url)
    #print(r.encoding)
    r.encoding='utf-8'
    html_code=r.text
    reg=re.compile(r'"objURL":"(.*?)"')
    imgs=re.findall(reg,html_code)
    # print(imgs)
    for img in imgs:
        #print(img)
        down_img(img)

def down_img(url):
    web_data=requests.get(url)
    filename=url.split('/')[-1]
    targetfile='./pict_baidu/{}'.format(filename)
    with open(targetfile,'wb') as f:
        f.write(web_data.content)

get_page()
