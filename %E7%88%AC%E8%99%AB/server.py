
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
        content  = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))+"<br>"
        content  = content + self.getTargetStr('btCoin')+"<br>"
        content  = content + self.getTargetStr('gf_Yl')+"<br>"
        content  = content + self.getTargetStr('gf_hs300')+"<br>"
        content  = content + self.getTargetStr('gf_fdc')+"<br>"
        content  = content + self.getTargetStr('gf_nadk')+"<br>"
        content  = content + self.getTargetStr('gold')+"<br>"
        content  = content + self.getTargetStr('rmb')+"<br>"

        
        self.wfile.write('<!DOCTYPE html><html><head><meta http-equiv="content-type" content="text/html;charset=utf-8"></head>'+content+'</html>')
      
        return

    def getTargetStr(self,targetId):
        targetName = db.get(targetId+':name')
        targetPrice = db.get(targetId+':price')
        return targetName+' ---- '+targetPrice

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('23.83.250.6', 8083), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()