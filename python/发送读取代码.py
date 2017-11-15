Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> 
>>> values={}
>>> values['username'] = "2570553846@qq.com"
>>> values['password'] = "tlnswd.3344"
>>> data = urllib.urlencode(values)
>>> url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
>>> request = urllib2.Request(url,data)
>>> response = urllib2.urlopen(request)
>>> print response.read(300)







<html>
  <head>
    <meta charset="utf-8" />
    <meta name="referrer" content="unsafe-url">
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta property="qc:admins" content="24530273213633466654" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

>>> 
