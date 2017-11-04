# coding:utf8

from lxml import etree
html = '''
 <ul>
    <li>1</li>
    <li title="text1">2</li>
    <li>1</li>
    <li title="text2">2</li>
    <li>1</li>
    <li title="text3">2</li>
    <li>1</li>
    <li title="text3 text4">2</li>
'''

xml = etree.HTML(html)

# 获取值为2的HTML节点
sec = xml.xpath('//ul/li')
sec_list = []
for sec_item in sec:
    if sec_item.text == '2':
        # print sec_item
        sec_list.append(sec_item)

# print sec_list

# 获取倒数第二个值为2的HTML节点
# print sec_list[-2]

# 编写简单代码遍历值为2的Html节点的title值
sec_title = xml.xpath('//ul/li/@title')

# print sec_title

# 请找出title属性中包含test3的HTML节点
for i in sec_title:
    if "text3" in i:
        j = i
        print j,type(j)
        print xml.xpath('//ul/li[@title=j]')

print xml.xpath('//ul/li[@title="text3"]')




