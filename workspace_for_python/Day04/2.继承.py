# 继承，子类继承父类，共享父类的属性和方法，并且自己可以做扩展

class Dog:
    def __init__(self,name):
        self.name = name
        print('我狗类的构造方法')

    def eat(self):
        print('%s狗吃东西'%(self.name))

class XTQ(Dog):             # 让XTQ类继承Dog类
    def eat(self):          # 方法的重写
        print("%s狗吃蟠桃"%(self.name))

xtq=XTQ("哮天犬")
print(xtq.name)
xtq.eat()   # 子类调用属性或方法时先要从子类本身去寻找，若子类没有就会从父类中寻找
