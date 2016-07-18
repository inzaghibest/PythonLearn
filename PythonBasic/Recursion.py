__author__ = 'zhangxp'
#递归
#阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print("factorial 10 = :" + str(factorial(10)))
#幂
def power(x, n):
    if n == 0:
        return 1
    else:
        return x*power(x, n-1)
#二分查找法
def BinarySearch(sequence, number, lower, upper):


