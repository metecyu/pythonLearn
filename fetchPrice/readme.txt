启动redis服务
redis-server /etc/redis/6379.conf
启动web服务
nohup python server.py > console.log 2>&1 &
启用定时程序
/sbin/service crond start
