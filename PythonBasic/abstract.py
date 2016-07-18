__author__ = 'zhangxp'

#斐波那契数列
#fibs = [0, 1]
#for i in range(8):
#    fibs.append(fibs[-2] + fibs[-1])
#print(fibs)
#创建函数

#def hello(name):
 #   'return hello name!'
 #   return 'hello ' + name + '!'
#print(hello('zhangxp'))

#文档字符串
#print(hello.__doc__)
#help(hello)

#函数的参数,当需要修改参数时
#def change(n):
#    n[0] = '12'
#names = ['34', '56']
#change(names)
#print(names[0])

#关键字参数
#def hello(name1, name2):
#    print (name1 + name2)

#关键字参数
#hello(name2 = 'zhangxp', name1 = 'hello')

# hello('python','zhangxp')
#收集参数(可变参数)
#def printpara(*params):
#    print(params)
#python语句前面不能有空格
#printpara('hello')

#处理关键字参数
#def prntpara1(**params):
#    printpara(params)
#prntpara1(x=1,y=2,z=3)
#def print_params(x,y,z=3,*param,**params):
#    print(x, y ,z)
#    print(param)
#    print(params)
#print_params(1,2,9,4,5,6,love='zhangxp')
#print_params(1,2)
#参数收集的逆过程
#def add(x,y):
#    return x+y
#params = (1,2)
#print(add(*params))

#def foo(x, y, z, m = 0, n = 0):
#    print(x, y, z, m, n)
#def call_foo(*param, **params):
#    print("call foo!")
#    foo(*param, **params)
#call_foo(1,2,3, m = 3, n = 4)

#x = 1
#scope = vars()
#scope['x']相当于变量x
#print(scope['x'])
#scope['x'] += 1
#print(x)

#x = 3
#def add(n):
#    global x
#    x+=n
#add(3)
#print(x)

# 函数的嵌套
def multiplier(factor):
    def multiplyByFactor(number):
        return factor*number
    return multiplyByFactor

print(multiplier(2)(3))