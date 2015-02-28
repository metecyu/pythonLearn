#coding=utf-8
'''
Created on 2013-3-4

@author: TonyYu
'''
# if语句
def tstIf():
    number = 23
    guess = int(raw_input('Enter an integer : '))
    if guess == number:
        print 'Congratulations, you guessed it.' # New block starts here
        print "(but you do not win any prizes!)" # New block ends here
    elif guess < number:
        print 'No, it is a little higher than that' # Another block
        # You can do whatever you want in a block ...
    else:
        print 'No, it is a little lower than that' 
        # you must have guess > number to reach here
    print 'Done'
        

if __name__ == '__main__':    

    tstIf()