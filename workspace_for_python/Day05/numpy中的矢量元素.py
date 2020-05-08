import numpy as np

# 矢量运算
arr = np.arange(1,10)
arr1 = arr**2
print(arr1)

# 通过numpy产生一个随机数的值
arr = np.random.randint(1,10,size=9)
arr = arr.reshape(3,3)
print(arr)

# 模拟500 次抛硬币
yingbi = np.random.randint(2,size=500)
print(np.where(yingbi==0,-1,1))
