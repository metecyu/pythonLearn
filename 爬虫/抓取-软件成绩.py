#coding=utf-8
import urllib    
import urllib2  
import cookielib  
import re
  
cookie = cookielib.CookieJar()    
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  
cookieJar = cookielib.CookieJar()                                      # 初始化一个CookieJar来处理Cookie的信息  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))  

pngCode = '0698';
cookieid = '78EA1627DC42FD6A8EC7613AF7CD6225'
#需要POST的数据#  
postdata=urllib.urlencode({    
    'table':'RKCJCX_RKCJCX',    
    'unitId':'100',
    'type':'2',
    'columns[0].property:':'',    
    'columns[0].code':'ZKZH',
    'columns[0].colType':'varchar2',
    'columns[0].operator':'1',
    'columns[1].property':'310115198210310111',
    'columns[1].code':'ZJH',
    'columns[1].colType':'varchar2',
    'columns[1].operator':'1',
    'columns[2].property':'2014年下半年'.encode("gbk"),
    'columns[2].code':'KSSJ',
    'columns[2].colType':'varchar2',
    'columns[2].operator':'1',
    'columns[3].property':'俞张平'.encode("gbk"),
    'columns[3].code':'XM',
    'columns[3].colType':'varchar2',
    'columns[3].operator':'1',
    'verifyData':pngCode
})  

#自定义一个请求#  
req = urllib2.Request(    
    url = 'http://119.254.106.102/bdrs/query/queryAction.do?method=customQuery',    
    data = postdata,
    headers = { 'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
                'Host': '119.254.106.102',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'http://119.254.106.102/bdrs/query/queryAction.do?method=customQuery',
                'Cookie': 'JSESSIONID='+cookieid,
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': '546'
            }  

)  
  
#访问该链接#  
result = opener.open(req)  
  
myPage = result.read()    

# print result.info()
# print result.getcode()

#encode的作用是将unicode编码转换成其他编码的字符串    
#decode的作用是将其他编码的字符串转换成unicode编码    
unicodePage = myPage.decode("gbk")    

#打印返回的内容#  
#print unicodePage  

myItems = re.findall('<tr>.*?<td valign="top">(.*?)</td>.*?<td>(.*?)</td>.*?</tr>',unicodePage,re.S)
#print myItems

for item in myItems:    
    itemTemp0 =  item[0].replace("\t", "").replace("\n", "").replace("\r", "")
    itemTemp1 =  item[1].replace("\t", "").replace("\n", "").replace("\r", "")
    print itemTemp0 ,":",itemTemp1
    

