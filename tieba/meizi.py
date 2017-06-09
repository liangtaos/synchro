#!/usr/bin/python
#coding:utf-8


import urllib,urllib2
import re
import lxml
import lxml.html


def getHtml(url):
    data = urllib2.urlopen(url)    
    return data.read()

def htmlRe(html):
    li = re.findall(r'<img src=(.*?) width="220" height="330" .*?>',html)
    n = 0
    for url_pic in li:
        print url_pic
        url_pic = url_pic.strip()
	url_pic = urllib.unquote(url_pic).encode('utf-8')
        url_pic = url_pic.split('"')[1]
        #ir = requests.get(url_pic)
        #sz = open('logo.jpg', 'wb').write(ir.content)
        #print sz
        #print urllib2.urlopen(url_pic).read()
        urllib.urlretrieve(url_pic,'/root/tongbu2/tieba/pic/%s.png'%n)
        n = n+1
        print n
def htmlRE(html, page):
    doc = lxml.html.fromstring(html)
    #nu = re.findall(r'\<a href=.*?\>(.*?)\<\/a\>\<em class="ch all"',html)
    #url = re.findall(r'\<a href=.*?\>\<img src="(.*?).jpg" alt=.*?\/\>\<\/a\>', html)
    src = doc.xpath('//div[@class="content"]/a/img/@src')[0].split('1.jpg')[0]
    nu = doc.xpath('//div[@class="page"]/a/text()')
    nu_number = []
    for i in nu:
	try:
	    n = int(i)
	    nu_number.append(n)
	except:
	    continue
    nu_max = max(nu_number)
    #print src
    #print nu_max
    #print nu, src,'*****************'
    
    for num in range(1,nu_max+1):
	url_ = src+'%s'%(num) +'.jpg'
        print url_
        urllib.urlretrieve(url_,'/root/tongbu2/tieba/images/pic%s/%s.png'%(page,num))
def main():
    for page in range(2,1000):
        url = 'http://www.mmjpg.com/mm/%s'%(str(page))
        os.system('mkdir /root/tongbu2/tieba/images/pic%s/'%page)
        html = getHtml(url)
        htmlRE(html,page)
   

if __name__ == '__main__':
    import os
    main()
