
#coding=utf-8
import urllib2
response = urllib2.urlopen('http://www.rkb.gov.cn/')  
html = response.read()  
# print html 
'''
'''

# 返回状态
print '===状态===：\n',response.getcode()

# 返回信息
print '===response信息===：\n\t',response.info()