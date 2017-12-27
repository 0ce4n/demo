# -*- coding"utf-8 -*-
import urllib
import urllib2
import re
class QSBK:
	def __init__(self):
		self.page = 1
		self.url = 'https://www.qiushibaike.com/8hr/page/'+str(self.page) 
		self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
		self.headers = {'User-Agent':self.user_agent}
		self.duanzi = []
		self.enable = False
	
	def getPage(self,page):
		self.url = 'https://www.qiushibaike.com/8hr/page/'+str(self.page)
		try:
			request = urllib2.Request(self.url,headers = self.headers)
			response = urllib2.urlopen(request)
			content = response.read().decode('utf-8')
			return content
		except urllib2.URLError,e:
			if hasattr(e,'reason'):
				print e.reason
				return None
				
	def getPageItems(self,page):
		content = self.getPage(page)
		if not content:
			print 'page load error'
			return None
		pattern = re.compile(r'<div.*?content.*?\n*<span.*?>\n*(.*?)\n*</span>.*?')
		items = re.findall(pattern,content)
		return items
		
	def loadPage(self):
		if self.enable == True:
			if len(self.duanzi) < 2:
				print self.url
				new_duanzi = self.getPageItems(self.page)
				if new_duanzi:
					self.duanzi.append(new_duanzi)
					self.page += 1
					
	def getoneduanzi(self,duanzi,page):
		for story in duanzi:
			input = raw_input()
			self.loadPage()
			if input == 'Q':
				self.enable = False
				return 
			print story
	
	def start(self):
		print "loding ,press Q exit"
		self.enable = True
		self.loadPage()
		nowPage = 0
		while self.enable:
			if len(self.duanzi)>0:
				duanzis = self.duanzi[0]
				nowPage += 1
				del self.duanzi[0]
				self.getoneduanzi(duanzis,nowPage)
				
spider = QSBK()
spider.start()