#coding=utf-8
'''
Created on 2013-3-4
@author: TonyYu
'''

# 循环数组
def forArray():
    x = [1,2,3,4]
    for i in x:
        print i
    else:
        print 'finished!'
        
# 循环一个String的char
def forString():
    x = 'Python'
    for i in x:
        print i 
        
# 循环范围
def forRange():
    # 输出  0 到 4
    for i in range(5):
        print str(i) + ' is the current value'
    else:
        print '--------------finished 1----------------'
        
    # 输出 2 到 7    
    for i in range(2,8):
        print  str(i) + ' is the current value'
    else:
        print '--------------finished 2----------------'
    # 输出 2 4 6 8       
    for i in range(2,9,2):
        print str(i) + ' is the current value'
    else:
        print '--------------finished 3----------------'

if __name__ == '__main__':    
    #forArray()
    #forString()
    forRange()