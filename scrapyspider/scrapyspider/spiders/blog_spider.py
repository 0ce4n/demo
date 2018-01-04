import scrapy
from scrapyspider.items import DemoItem
import scrapy

class BlogSpider(scrapy.Spider):
	name = 'woodenrobot'
	start_urls = ['http://woodenrobot.me']

	def parse(self, response):
		print response
