# -*- coding: utf-8 -*-
import urllib
import urllib2
import re

url = 'http://flxx.ls114.cn/rjgcs/'
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
p = 0
j = 0
content_pattern = re.compile('<font style.*?>(.*?)</font>', re.S) #爬取标题行
content_list = re.findall(content_pattern, html)
content_pattern1 = re.compile('<td width.*?>(.*?)</td>', re.S)    #爬取编号、分类和时间
content_list1 = re.findall(content_pattern1, html)

for item in content_list:                                         #进入循环，有多少个标题行循环多少次
    print '\n'
    print content_list[j]                                         #依次输出标题行
    j = j + 1                                                     #标题行数组位累加一
    p = p + 3                                                     #编号、分类和时间三个数组位

    for i in range(0,3):                                          #将爬取出的编号、分类和时间三个连续接在标题行下输出
        print content_list1[i + p - 3]

    input = raw_input()                                           #按一次回车输出一个，按“e”退出
    if input == "e":       
        break
    print "******************************下一个******************************\n"
   
