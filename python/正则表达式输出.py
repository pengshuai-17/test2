Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: C:/Users/lenovo32/Desktop/11.py ==================
>>> y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
>>> import re
>>> re.findall('\w+@(qq|163|126).com', y)
['qq', '163', '126']
>>> re.findall('\w+@(?:qq|163|126).com', y)
['123@qq.com', 'aaa@163.com', 'bbb@126.com']
>>> y = 'tel:010-12345678 address:changanRoad'
>>> re.findall('\d', y)
['0', '1', '0', '1', '2', '3', '4', '5', '6', '7', '8']
>>> re.findall('\d+', y)
['010', '12345678']
>>>  re.findall('\d+-', y)
 
  File "<pyshell#7>", line 2
    re.findall('\d+-', y)
    ^
IndentationError: unexpected indent
>>> re.findall('\d+-', y)
['010-']
>>> re.findall('\d+-\d+', y)
['010-12345678']
>>> phone = "2004-959-559 # 这是一个国外电话号码"
>>> re.findall('\d', phone)
['2', '0', '0', '4', '9', '5', '9', '5', '5', '9']
>>> re.findall('\d-\d-\d', phone)
[]
>>> re.findall('\d+-\d+-\d', phone)
['2004-959-5']
>>> re.findall('\d+-\d+-\d+', phone)
['2004-959-559']
>>> phone = '2004-959-559,569-64-488,48548748'
>>> re.findall('\d+-\d+-\d+', phone)
['2004-959-559', '569-64-488']
>>> 
