import scrapy
from scrapyspider.items import DemoItem

class BlogSpider(scrapy.Spider):
	name = 'woodenrobot'
	start_urls = ['http://woodenrobot.me']

	def parse(self, response):
		print response
