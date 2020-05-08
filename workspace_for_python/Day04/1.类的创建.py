# python中类的创建
# python中如何定义类中的方法 def 方法名（self，形参）
# 对象的创建语法：对象=类名（）
# 对象的使用通过“.”


class Person:
    def __init__(self,name,age):
        """
        构造方法（创建对象，初始化对象）
        self是指当前类对象
        """
        self.name = name
        self.age = age
        print("我是人类的构造方法")

    def introduce(self):
        print("我叫{},我今年{}岁".format(self.name,self.age))

    def __str__(self):
        print("姓名：{},年龄：{}岁".format(self.name, self.age))

# 1.对象的创建使用Person（）
admin = Person('admin',18)   # p是通过类中的构造方法创建出的人对象
# 2.'admin',18是实参（实际存在的参数）
zhangsan = Person('张三',45)
# 3.对象的调用用.读作的，成员访问符

# print(admin.name,admin.age)     # 对象.属性
#
#
# admin.introduce()   # 对象.方法


print(admin)     # 打印对象时会默认调用类中的__str__()方法，把对象的地址转换成所有属性的字符串




