# -*- coding:utf-8 -*-
import re
from bs4 import BeautifulSoup
html="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse 123123"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister sister2" id="link 1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<div data-foo="value">foo!</div>
</body>
"""
#将网页的html内容创建为一个BS对象，文档被转化为unicode，并且整个html的实例都被转化为unicode代码
soup = BeautifulSoup(html,"html.parser")

#格式化html内容
print soup.prettify()
print ""

print soup.name

#对象的种类常用的分为Tag、Name、Attributes
#获取一个tag
tag = soup.p
print tag

#获取name
tag_name = tag.name
print tag_name

#获取tag的属性Attributes
tag_attrs = tag.attrs
print tag_attrs
#例如tag有class属性等多种属性
tag_atb = tag['class']
print tag_atb

tag_atb = tag['name']
print tag_atb
#tag的属性的操作方法与字典一样
tag['class'] = 'haha'
del tag['name']
print tag

#在BS中多值类型的返回时list，若在HTML定义中为规定某属性是多值的，则BS认为其实字符串
tag = soup.a
print tag
print tag['class']
print tag['id']

#tag内的字符串，BS用NavigableString来包装tag中的字符串
tag = soup.b
print tag.string
print type(tag.string)

#tag中的字符串不能编辑，但是可以被替换，用replace_with
tag.string.replace_with('hahahahaha!')
print tag.string	
#NavigableString 对象支持 遍历文档树 和 搜索文档树 中定义的大部分属性, 并非全部.尤其是,一个字符串不能包含其它内容(tag能够包含字符串或是其它tag),字符串不支持 .contents 或 .string 属性或 find() 方法.

#注解,comment对象是一个特殊的类型
tag = soup.a
print tag.string
print type(tag.string)
#当comment在html文档中时，他会以特殊的方式输出
print tag.prettify()

#遍历文档树
#获取tag内容
print soup.head
print soup.head.title

#.contents可以将tag的子节点以列表形式列出来
tag = soup.body
print tag.contents

#通过.children生成器，可以对tag的子节点进行遍历
for child in tag.children:
	print child

#.descendants 属性可以对所有tag的子孙节点进行递归循环
for child in tag.descendants:
    print child

	
#如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点
tag = soup.p
print tag.string

#如果tag中包含多个字符串 [2] ,可以使用 .strings 来循环获取
print '-------------------------------------------------'
tag = soup.body
for string in tag.strings:
	print string

#使用 .stripped_strings 可以去除多余空白内容
tag = soup.body
for string in tag.stripped_strings:
	print string

#.parent,.parents等具体看官方文档

#文档编码格式
print soup.original_encoding

#搜索文档树
#find()以及find_all()
#过滤器的类型：字符串
print '-------------------------------------------------'
tag = soup.find_all('p')
print tag
#过滤器的类型：正则表达式
print '-------------------------------------------------'
tag = soup.find_all(re.compile(r'^b'))
print tag
#过滤器的类型：列表
print '-------------------------------------------------'
tag = soup.find_all(['a','b'])
print tag
#过滤器的类型：True
print '-------------------------------------------------'
tag = soup.find_all(True)
print tag
#过滤器的类型：方法
print '-------------------------------------------------'
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
tag = soup.find_all(has_class_but_no_id)
print tag


#find_all( name , attrs , recursive , string , **kwargs )
#name 参数可以查找所有名字为 name 的tag.搜索 name 参数的值可以使任一类型的 过滤器 ,字符窜,正则表达式,列表,方法或是 True .
#如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性.
#搜索指定名字的属性时可以使用的参数值包括 字符串 , 正则表达式 , 列表, True 
tag = soup.find_all(id='link2')
print tag

#使用多个指定名字的参数可以同时过滤tag的多个属性:
tag = soup.find_all(href=re.compile("lacie"), id='link2')
print tag

#有些tag属性在搜索不能使用,但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag:
tag = soup.find_all(attrs={"data-foo": "value"})
print tag
	
#按CSS进行搜索  class_
#class_ 参数同样接受不同类型的 过滤器 ,字符串,正则表达式,方法或 True :
tag = soup.find_all("a", class_="sister")
print tag

#通过 string 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, string 参数接受 字符串 , 正则表达式 , 列表, True . 
tag = soup.find_all(string="Lacie")
print tag

#limit参数find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.
tag = soup.find_all("a", limit=2)
print tag

#调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False .
tag = soup.html.find_all("title", recursive=False)
print tag

#find_all()可以简写soup.find_all("a")和soup("a")等价

#find(),与find_all类似，不过find()方法直接返回结果，而find_all()返回的是列表





