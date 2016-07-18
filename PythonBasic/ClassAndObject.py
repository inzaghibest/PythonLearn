__author__ = 'zhangxp'
class person:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print("hello world! I'm %s"%self.name)
foo = person()
foo.setName('zhangxp')
foo.greet()
class Bird:
    song = 'song!'
    def sing(self):
        print(self.song)
bird = Bird()
bird.sing()
birdSing = bird.sing
birdSing()