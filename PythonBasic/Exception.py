__author__ = 'zhangxp'
#引发异常
#raise Exception
#raise Exception('Excepiton Test')
dir(Exception)

#try/except
try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    z = int(x)/int(y)
except ZeroDivisionError:
    print("The second number can't be zero")