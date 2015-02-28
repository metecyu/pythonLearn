#coding=utf-8
import re  
'''
# 获取匹配的的内容
'''
p = re.compile(r'\d+')  
print '找出所有的数字',p.findall('one1two2three3four4')  

'''
# 获取匹配的的内容-比较复杂的例子
'''
unicodePage ='<div class="content" title="2015-02-22 00:08:46">i am a boy</div><div class="content" title="2015-02-22 00:08:46">i am a girl</div>'
myMatchStr = re.findall('<div.*?class="content".*?title=".*?">.*?</div>',unicodePage,re.S)
print '普通：',myMatchStr

'''
   获取匹配的的内容-比较复杂的例子 分组写法（对象数组形式）
'''
myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage,re.S)
print '分组-对象数组：',myItems
items = []    
""" """
for item in myItems:    
    print  item[0].replace("\n","")
    print  item[1].replace("\n","")
                   