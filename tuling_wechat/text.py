# -*- coding: utf-8 -*-  
import urllib  
import json  
import requests
def getHtml(info):
    key = '5af3fe7e2f9f40058c1452651c07fd33'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' 
    request = api + info 
    page = requests.get(request)  
    html = page.text
    dic_json = json.loads(html)
    text = dic_json['text']  
    if dic_json.get('url'):
        data = text,dic_json['url']
        data = str(data)
        return data
    elif dic_json.get('list'):
        data = text,dic_json['list']
        data = str(data)
        return data
    else:
        return text  
  
if __name__ == '__main__':  
    #key = '5af3fe7e2f9f40058c1452651c07fd33'  
    #api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='   
    #info = raw_input('我: ')  
    #request = api + info 
    #print request 
    #response = getHtml(request)  
    #dic_json = json.loads(response)  
    #print '机器人: '.decode('utf-8') + dic_json['text']  
    while 1:
        info = input('我: ')
        print(getHtml(info))
