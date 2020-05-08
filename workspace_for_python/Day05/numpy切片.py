# numpy切片操作（切片操作的是索引）
import numpy as np
# 切片
arr = np.arange(1,10)

print(arr)

print(arr[0:3])
print(arr[3:])
print(arr[0:9:2])

print(arr[1::2])
print(arr[::-2])  # 步长若为一个步数，则倒序切

# 深浅拷贝
# 浅拷贝（引用地址，地址中的与那素改变时，变量指向的内容也会改变）
# 深拷贝 arr.copy()
print(arr)
arr8 = arr[:]
arr9 =arr.copy()
arr[0] = 6
print(arr)
print(arr8)
print(arr9)

# 花式索引切片
arr = np.arange(1,10)
index =[0,3,4,5,7]
print(arr[index])