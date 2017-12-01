# -*- coding: utf-8 -*-
import urllib
import urllib2
import re


url = 'http://flxx.ls114.cn/jq/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = { 'User-Agent' : user_agent }
 
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

        
content_pattern = re.compile('<font style.*?>(.*?)</font>', re.S)
content_list = re.findall(content_pattern, html)
for item in content_list:
    print item


content_pattern = re.compile('<td width.*?>(.*?)</td>', re.S)
content_list = re.findall(content_pattern, html)
for item in content_list:
    print item
