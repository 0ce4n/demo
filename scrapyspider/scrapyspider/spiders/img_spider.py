# -*- coding:utf-8 -*-
import scrapy
from scrapyspider.items import ImageItem
from bs4 import BeautifulSoup

class ImageSpider(scrapy.Spider):
	name = 'imgspider'
	
	start_urls = ['http://7xnzbp.com2.z0.glb.qiniucdn.com/wp-content/uploads/2014/10/pt-sdn-Open-vSwitch%EF%BC%88OvS%EF%BC%89%E6%BA%90%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90%E4%B9%8B%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B%EF%BC%88%E6%94%B6%E5%8F%91%E6%95%B0%E6%8D%AE%E5%8C%85%EF%BC%892014-10-31.jpg']
	
	def parse(self, response):
		with open('a.jpg',"w+") as fp:
			fp.write(response.body)