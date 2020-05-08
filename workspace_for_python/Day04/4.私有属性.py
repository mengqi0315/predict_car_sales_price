# 私有属性

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age


a=Animal("dog",10)
print(a.age)
a.age=-1
print(a.age)
print('-'*50,'这是一条分割线')
# 上面这种形式非常不安全，所有我们引入私有属性

class Animal1:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def  get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name
a=Animal1("旺财",8)
print(a.get_name())
a.set_name("小狗")
print(a.get_name())



