# 导入numpy模块
import numpy as np
# 通过numpy创建一维数组,可以放列表，和元组，不能放集合和字符串np.array(list/tuple)
lst = [1.3,2,3,4,5]
arr = np.array(lst)
# print(lst)
# print(arr)
# print(arr[1])

tup = ('a','b','c')
arr = np.array(tup)
# print(arr)

dic= {'kw':'python','start':1,'end':4}
arr = np.array(dic)
# print(arr)

char = np.array('abcef')
# print(char)

se ={1,2,3,4,6,6,6}
se = np.array(se)
# print(se)
arr = np.array(lst)
# 2. 获取数组元素的类型(int,float)
# print(arr[0].dtype)
arr=np.arange(1,10,1,float)
arr = np.arange(10)
print(arr)

# 4.产生一个二维数组(必须行列对应)
lst = [[1,2,3],[4,5,6]]
print(lst)
arr2 = np.array(lst)
print(arr2)

# 5.常用的产生二维数组的方法（一维转二维）
arr = np.arange(1,13).reshape(6,-1)
print('秩',np.ndim(arr))
print(arr)
print(arr.shape)

print(arr.ndim)
print(arr.dtype)

print("-"*50,'这是一条分割线')
a = np.arange(15).reshape(3,5)
