import numpy as np
import pylab
import math
import random
# 1.reshape()重构
a=np.arange(15).reshape(3,5)
print(a)
# 2.返回数组结构
print(a.shape)
# 3.返回数组的维数
print(a.ndim)
# 4.dtype.name itemsize size 分别表示数组中各个元素的类型，数组中每个元素的字节大小，以及数组元素的总个数
print(a.dtype.name,a.itemsize,a.size)

# 5.通过列表创建数组
a= [1.3,2,3,4,5]
arr = np.array(a)
print('列表创建的数组：是{}'.format(arr))

# 6.创建特殊数组
a = np.zeros((3,4))
print(a)
a = np.ones((2,3,4),dtype='int16')
print('全1数组',a)
a = np.empty((2,3))
print(a)

# 7.数组支持向量运算
arr = np.arange(1,10)
arr1 = arr**2
print(arr1)

# 8. 索引切片
arr = np.arange(1,10)
print(arr)
print(arr[0:3])     # 0-3个元素
print(arr[3:])    # 从第三个元素往后切
print(arr[0:9:2])    # 设置步长
print(arr[1::2])
print(arr[::-2])  # 步长若为一个步数，则倒序切

#  9.迭代器
arr = np.arange(1,10)
for element in arr.flat:
    print(element)

# 9.形状操作
arr = np.random.randint(1,10,size=12)
arr = arr.reshape(3,4)
print(arr)

# 10.复制和视图
a = np.arange(12)     # 完全不复制，没有创建新的对象
b = a
print(b is a)
c = a.view()
print('c is a?{}'.format(c is a))
print('c.base is a? {}'.format(c.base is a))

a = np.arange(12)
d = a.copy()                     # 创建了一个新的数组
print('d is a? {}'.format(d is a))

# numpy使用技巧
a = np.arange(30)
a.shape=2, -1, 3         # -1表示缺失的维度
print(a)

# 向量组合
x = np.arange(0,10,2)
y = np.arange(5)
m = np.vstack([x,y])
print(m)
xy = np.hstack([x,y])
print(xy)



