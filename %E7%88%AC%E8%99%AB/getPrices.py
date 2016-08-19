
#coding=utf-8

import requests
import re
import json
import redis
#下面三行是编码转换的功能，大家现在不用关心。
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

db = redis.Redis(host='localhost',port=6379,db=0)



def fetchOne(targetId,targetName,targetUrl,regStr):    


  #hea是我们自己构造的一个字典，里面保存了user-agent
  head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
  html = ''
  try:
    html = requests.get(targetUrl,headers = head)
  except IOError:
    return 
  #print html.status_code
  html.encoding = 'utf-8' #这一行是将编码转为utf-8否则中文会显示乱码。 
  prices = re.findall(regStr,html.text,re.S)
  
  targetPrice = ''
  for priceTemp in prices:
      targetPrice = priceTemp

  targetName = targetName.encode('utf-8')
  targetPrice = targetPrice.encode('utf-8')
  print(" %s \t\t %s" %(targetName,targetPrice)) 
  # store to redis 
  db.set(targetId+':name',targetName)
  db.set(targetId+':price',targetPrice)
  

fetchOne('btCoin',u'比特币:','https://www.okcoin.cn','<em class="indexBtcPrice">(.*?)</em>')
fetchOne('gf_Yl',u'广发医疗:','http://fund.eastmoney.com/001180.html','id="gz_gsz">(.*?)</span>')
fetchOne('gf_hs300',u'广发沪深300:','http://fund.eastmoney.com/270010.html','id="gz_gsz">(.*?)</span>')
fetchOne('gf_fdc',u'广发美国房地产:','http://fund.eastmoney.com/000179.html','id="gz_gsz">(.*?)</span>')
fetchOne('gf_nadk',u'广发美纳斯达克:','http://fund.eastmoney.com/270042.html','id="gz_gsz">(.*?)</span>')
fetchOne('gold',u'黄金:','http://www.cngold.org/xhhj/','class=\'JO_38493q63\'>(.*?)</td>')
fetchOne('rmb',u'人民币:','http://www.x-rates.com/table/?from=CNY&amount=1','href=\'/graph/\?from=USD&amp;to=CNY\'>(.*?)</a>')





#unicode_str = u'中文'
#unicode_str =unicode_str.encode('utf-8')
#print unicode_str

#fetchOne('bt哈:','https://www.okcoin.cn','<em class="indexBtcPrice">(.*?)</em>')
#fetchOne('yil:','http://fund.eastmoney.com/001180.html','id="gz_gsz">(.*?)</span>')
#fetchOne('300:','http://fund.eastmoney.com/270010.html','id="gz_gsz">(.*?)</span>')
#fetchOne('fdc:','http://fund.eastmoney.com/000179.html','id="gz_gsz">(.*?)</span>')
#fetchOne('nsdq:','http://fund.eastmoney.com/270042.html','id="gz_gsz">(.*?)</span>')
