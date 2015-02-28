#coding=utf-8

'''
Created on 2013-2-25
@author: TonyYu
'''
class people:
    name = ""  
    age = 0  
    def __init__(self,n,a):  
        self.name = n  
        self.age = a  
    
    '''
            说方法
    '''
    def speak(self):
        print("我是 %s， 今年%d" %(self.name,self.age))  

'''
main 方法
'''
if __name__ == '__main__':
    pass
    p = people('俞xx',30)  
    p.speak()  