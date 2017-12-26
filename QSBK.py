#-*- coding:utf-8 -*-
import urllib
import urllib2

#https://www.qiushibaike.com/8hr/page/2/
page = 1
url = 'https://www.qiushibaike.com/'
user_agent = r'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
headers = {'User-Agent': user_agent}
try:
	request = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(request)
	print response.read()
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason         
