import pandas as pd
import numpy as np
from pandas import Series,DataFrame

# Series类似于一位数组，它由一组数据以及对应的数据标签（即索引）组成，通常来说，仅仅由一组数据就可以产生最基本的series
obj = pd.Series([4,7,-5,3])
print(obj)
# 通过values 和 index 这两个属性获取数组的值和索引对象
print(obj.values)
print(obj.index)

# 创建有标记的索引
obj = pd.Series([4,7,-5,3],index=['d','b','a','c'])
print(obj['a'])

# 可以将Series看成是一个长度固定的有序字典，字典反应的是索引值到数据值的映射
# 在以字典作为参数的函数中，也可以用Serise代替字典作为函数的参数
data={'Oregon':1000,'a':2000,'Ohio':3000,'Texas':4000}
data=pd.Series(data)
print(data)

states = ['California','Ohio','Oregon','Texas']
datas = pd.Series(data,index=states)
print(datas)

# 缺失值检测
print(pd.isnull(datas))
print(pd.notnull(datas))


# Series 可以自动对齐索引
sdata = {'Ohio':3500,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3 = pd.Series(sdata)

states = ['California','Ohio','Oregon','Texas']
obj4 = pd.Series(sdata,index=states)
print(obj3)
print(obj4)

print(obj3+obj4)

# DataFrame用来处理表格类型的数据结构，含有一组有序的列，每一列可以是不同类型的值，可以按行索引或按列索引，
data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002],'pop':[1.5,1.7,3.6,2.4,2.9]}
frame = pd.DataFrame(data)
print(frame)

frame = pd.DataFrame(data,columns=['year','state','pop'])
print(frame)

# 与Series类似，若传入的列名找不到那么就会产生NA列的值
frame2 = pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five'])
print(frame2)
# 获取某一列
print(frame2.year)
# 获取某一行
print(frame2.ix['three'])

# 对空列赋固定值
frame2['debt'] = 16.5
print(frame2)
#对空列赋一系列的值
frame2['debt'] = np.arange(5)
print(frame2)

# 如果赋值时长度缺失，空位会补上NaN
val = pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt'] = val
print(frame2)
# 可以对不存在的新列进行赋值，从而构造出一个新列，
frame2['eastern'] = frame2.state =='Ohio'
print(frame2)

# 删除某一列
del frame2['eastern']
print(frame2.columns)