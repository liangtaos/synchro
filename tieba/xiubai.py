#!/usr/bin/python
#coding:utf-8

import urllib2, urllib
import lxml
import lxml.html
import random
import time
hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]


#class MySpider(object):
#    def __init__(self, url):
#        self.url = url
#
#    def 

f = open('./xiubai.txt','w')
def main():
    for i in range(1,36):
        url = 'https://www.qiushibaike.com/text/page/%s/?s=4989982'%(str(i))
        req = urllib2.Request(url, headers=random.choice(hds))
        try:
            source_code = urllib2.urlopen(req,timeout=10).read()
            print '出错了%s页'%(i)
        except:
	    time.sleep(10)
            try:
	        source_code = urllib2.urlopen(req,timeout=10).read()
            except:
		print '不要第%s页'%(i)
	        continue
	#source_code
        doc = lxml.html.fromstring(source_code)
        text = doc.xpath('//div[@class="content"]/span/text()')
        #print text,'$'*50
        for line in text:
            line = line.encode('utf-8')
            print line
	    f.write(line+'\n')
        print '已经下载了%s页'%(i)
        time.sleep(3)
    f.close()    
if __name__ == '__main__':
    main()
