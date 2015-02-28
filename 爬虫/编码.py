#coding=utf-8
import re  
import sys

'''
    编码
'''
print '系统编码:'+sys.getdefaultencoding()  

print '是否utf编码：',isinstance('考试时间', unicode) 
print '是否utf编码  （添加u）：',isinstance(u'考试时间', unicode) 

# 默认编码方式 utf-8                                    
rkPage ='考试时间1'
myItems = re.findall('考试时间',rkPage,re.S)
print '中文匹配结果：',myItems

myItems = re.findall('\xe8\x80\x83\xe8\xaf\x95\xe6\x97\xb6\xe9\x97\xb4',rkPage,re.S)
print '编码匹配结果：',myItems


# 指定unicode编码
rkPage =u'考试时间'
myItems = re.findall(u'考试时间',rkPage,re.S)
print '中文匹配结果：',myItems

myItems = re.findall(u'\u8003\u8bd5\u65f6\u95f4',rkPage,re.S)
print '编码匹配结果：',myItems


# 这里说明 encode方法的机制 和 findall还是不同，这里不管str的保存编码如何，都能顺利的转换为标准的utf-8 asc编码
str = b'e88083'  # 实际就是 asc 2编码
print str.decode("hex") 
str2 = "考111aaa室"
for item in str2:  
    print item.encode("hex")  #每个汉子 使用3个字节
    
# 这里说明 encode方法的机制 和 findall还是不同，这里不管str的保存编码如何，都能顺利的转换为标准的utf-8 asc编码
str = u"\u8003"
print 'unicode:',str.encode("hex") 
str = "考"
print 'utf-8:',str.encode("hex") 



# 编码转换 
#  print '\xe8\x80\x83\xe8\xaf\x95\x31\x61\x31\xe6\x97\xb6\xe9\x97\xb4'.encode('utf-8')
