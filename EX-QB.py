# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class EXQB:
	queue = []
	host = 'https://www.qiushibaike.com'
	def __init__(self):
		self.page = 1
		self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
		self.headers = {'User-Agent':self.user_agent}
		self.enable = False
		self.fo = open("QB.txt","w+")
		
	def getcontent(self,url):
		request = urllib2.Request(url,headers = self.headers) 
		try:
			response = urllib2.urlopen(request,timeout = 5)
			content = response.read().decode('utf-8')
			return content
		except urllib2.URLError, e:
			if hasattr(e,'reason'):
				print e.reason
				return False
		
	def addqueue(self,page):
		url = EXQB.host+'/8hr/page/' + str(page)
		content = self.getcontent(url)
		if content:
			print "抓取段子列表..."
			pattern = re.compile(r'<a.*?href="(/article.*?)".*?<div.*?content.*?>',re.S)
			url_list = re.findall(pattern,content)
			self.queue += url_list
			return True
		else:
			return False
		
				
	def checkqueue(self):
		if len(self.queue) < 2:
			self.page += 1
			if not self.addqueue(self.page):
				return False	
			if self.page > self.count:
				self.enable = False	
		return True
			
	def getMessage(self):
		if self.checkqueue():
			url = self.host + self.queue[0]
			del self.queue[0]
			print "爬取url："+url
			content = self.getcontent(url)
			if content:
				print "抓取段子中..."
				pattern1 = re.compile(r'<h2>(.*?)</')
				items = re.findall(pattern1,content)
				if items[0] == '匿名用户':
					print '匿名用户'
					return None
				pattern = re.compile(r'<div.*?author.*?<h2>(.*?)</.*?<div.*?Gender (.*?)Icon.*?>(.*?)</.*?content">(.*?)</div>',re.S)
				items = re.findall(pattern,content)
				item = items[0]
				if item:
					if item[1]=='man':
						item_new = item + ('男',)
					else:
						item_new = item + ('女',)
				return item_new
			else:
				print "获取网页内容失败"
		else:
			print "获取url列表失败"
			return None
	
	def writefile(self):
		items = self.getMessage()
		if items:
			print "写入文件中..."
			self.fo.write('用户名：'+items[0]+'\n性别：'+items[4]+'\n年龄：'+str(items[2])+'\n内容：\n'+items[3])
			self.fo.write('------------------------分隔符----------------------------------------\n')
			return True
		else:
			return False
				
				
	def star(self):
		self.enable = True
		self.count = 10
		self.addqueue(self.page)
		while len(self.queue)>0 and self.enable:
			self.writefile()
			

aa = EXQB()
aa.star()
		
		
