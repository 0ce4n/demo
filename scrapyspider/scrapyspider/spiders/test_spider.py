# -*- coding: utf-8 -*-
import scrapy
from scrapyspider.items import TestItem
from bs4 import BeautifulSoup


class TestSpider(scrapy.Spider):
	"""
	测试爬虫
	"""
	name = 'testspider'

    #start_urls = ['https://www.qiushibaike.com/']
	def _get_gender(self, item):
		if item == 'manIcon':
			return u'男'
		return u'女'

	def parse(self, response):
		Item = TestItem()
		soup = BeautifulSoup(response.body, "html.parser")
		items = soup.find_all("div", class_='article')
		for item in items:
			try:
				Item['user_name'] = item.find("h2").string
				Item['user_age'] = item.find("div", class_='articleGender').string
				Item['user_gender'] = self._get_gender(item.find("div", class_='articleGender')['class'][1])
				Item['user_content'] = item.find("span").string
				yield Item
			except:
				print "error!"

	def start_requests(self):
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
		headers = {'User-Agent': user_agent}
		url = 'http://www.qiushibaike.com/'
		return [scrapy.http.Request(url, headers=headers, callback=self.parse)]
