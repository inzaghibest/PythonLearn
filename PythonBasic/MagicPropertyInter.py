__author__ = 'zhangxp'

#这句话会将所有类为新式类,所谓新式类就是隐式或显示设置超类object
#在python3.0之后不加这句话也会自动设置
#__metaclass__ = type
#class NewStyle(object):
#    pass
#class OldStyle:
#    pass
#构造函数
#class fooBar:
#    def __init__(self, value = 4):
#        self.someVar = value
#foo = fooBar(5)
#print(foo.someVar)
#class A:
#    def hello(self):
#        print("hello A!")

#class B(A):
#    def hello(self):
#        print("hello B!")
#class B(A):
#    pass
#a = A()
#b = B()
#a.hello()
#b.hello()

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("eat...")
            self.hungry = False
        else:
            print("no thanks!")

class Songbird(Bird):
    def __init__(self):
        #bird.__init__(self)
        super(Songbird, self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

sb = Songbird()
sb.eat()
sb.sing()


