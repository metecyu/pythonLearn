
#coding=utf-8
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import redis
import time
db = redis.Redis(host='localhost',port=6379,db=0)

class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        self.send_response(200)
        self.end_headers()
        content = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))+"<br><br>"
        content += self.getTargetStr('btCoin')+"<br>"
        content += self.getTargetStr('gf_Yl')+"<br>"
        content += self.getTargetStr('gf_hs300')+"<br>"
        content += self.getTargetStr('gf_fdc')+"<br>"
        content += self.getTargetStr('gf_nadk')+"<br>"
        content += self.getTargetStr('gold')+"<br>"
        content += self.getTargetStr('rmb')+"<br>"


        htmlStr = '<!DOCTYPE html><html>'
        htmlStr +=  '<head><meta http-equiv="content-type" content="text/html;charset=utf-8"></head>'
        htmlStr +=  '<body style="font-size:30px">'
        htmlStr +=  content
        htmlStr +=  '</body>'
        htmlStr +=  '</html>'



        self.wfile.write(htmlStr)
            
      
        return

    def getTargetStr(self,targetId):
        targetName = db.get(targetId+':name')
        targetPrice = db.get(targetId+':price')
        return targetName+' ---- '+targetPrice

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    #server = HTTPServer(('23.83.250.6', 8083), GetHandler)
    server = HTTPServer(('localhost', 8083), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()