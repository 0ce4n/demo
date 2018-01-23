# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DemoItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()

class TestItem(scrapy.Item):
	user_name = scrapy.Field()
	user_gender = scrapy.Field()
	user_age = scrapy.Field()
	user_content = scrapy.Field()
	user_img_url = scrapy.Field()

class ImageItem(scrapy.Item):
	img_name = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field()