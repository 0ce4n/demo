# -*- coding: utf-8 -*-
import scrapy
from scrapyspider.items import TestItem
from bs4 import BeautifulSoup
import re

class testspider(scrapy.Spider):
	name = 'testspider'
	#start_urls = ['https://www.qiushibaike.com/']
	
	def parse(self,response):
		Item = TestItem()
		soup = BeautifulSoup(response.body,"html.parser")
		items = soup.find_all("div",class_=re.compile(r'article.*'))
		for item in items:
			Item['user_name'] = item.find("h2").string.encode('utf-8')
			Item['user_age'] = item.find("div",class_=re.compile(r'articleGender.*')).string.encode('utf-8')
			Item['user_gender'] = "boy"
			Item['user_content'] = item.find("span").string.encode('utf-8')
			yield Item
			
	def start_requests(self):
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
		headers = {'User-Agent': user_agent}
		url = 'http://www.qiushibaike.com/'
		return [scrapy.http.Request(url,headers = headers,callback = self.parse)]