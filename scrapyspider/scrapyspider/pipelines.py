# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem

class ScrapyspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class TestPipeline(object):
    def __init__(self):
        self.man_fp = open('man.json','wb')
        self.woman_fp = open('woman.json','wb')

    def process_item(self, item, spider):
        if item['user_gender'] == 'man':
            line = json.dumps(dict(item)) + '\n'
            self.man_fp.write(line)
        if item['user_gender'] == 'woman':
            line = json.dumps(dict(item)) + '\n'
            self.woman_fp.write(line)
        return item
        
    def open_spider(self,spider):
        self.man_fp.write(spider.name+'\n')
        self.woman_fp.write(spider.name+'\n')
    
    def close_spider(self,spider):
        self.man_fp.write(spider.name+' close \n')
        self.woman_fp.write(spider.name+' 关闭 \n')
        self.man_fp.close
        self.woman_fp.close

class Test2Pipeline(object):
    def process_item(self, item, spider):
        if item['user_gender'] == 'man':
            raise DropItem("Drop this item")
        return item