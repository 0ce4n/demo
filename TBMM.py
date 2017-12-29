# -*- coding:utf-8 -*-

import urllib2
import urllib
import re
import os
import tool

class TBMM:
	def __init__(self):
		self.site = 'https://mm.taobao.com/json/request_top_list.htm?'
		self.tool = tool.Tool()
		
	def getcontent(self,page):
		url = self.site + str(page)
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		return response.read().decode('gbk')
	
	def getMM(self,page):
		MM = self.getcontent(page)
		pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
		items = re.findall(pattern,MM)
		MMs = []
		for item in items:
			MMs.append([item[0],item[1],item[2],item[3],item[4])
		return MMs
		
	def getdetailpage(self,url):
		request = urllib2.Requset(url)
		response = urllib2.urlopen(request)
		return response.read().decode('gbk')
		
	def getMMdsc(self,content):
		pattern = re.compile(r'<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
		result = re.search(pattern,content)
		return self.tool.replace(result.group(1))
	
	def getimg(self,page):
		pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
		content = rel.search(pattern,page)
		patternImg = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
		images = re.findall(patternImg,content.group(1))
		
	def saveImg(self,images,name):
		number = 1
		print "发现"+name+共有+len(images)+张照片
		for imageurl in images:
			splitPath = imageurl.split('.')
			fTail = splitPath.pop()
			if len(fTail)>3:
				fTail = "jpg"
			filename = name+ "/" +str(number)+"."+fTail
			self.saveImg(imageurl,filename)
			nember += 1
			
	def saveMM(self,content,name):
		fileName = name+"/"+name+".txt"
		f = open(fileName,"w+")
		pirnt "保存个人信息"+fileName
		f.write(content.encode('utf-8'))
	
a = TBMM()
a.getMM(1)