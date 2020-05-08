# 多继承


class Dog:
    def __init__(self,name):
        self.name = name


    def eat(self):
        print('%s狗吃东西'%(self.name))


class God:
    def fly(self):
        print("可以上天入地")

class XTQ(Dog,God):
    def __init__(self,name):
        Dog.__init__(self,name)
xtq=XTQ("哮天犬")
print(xtq.name)
xtq.eat()
xtq.fly()