#coding=utf-8
import random

import numpy as np

t1=np.array([1,2,3,4])
print(t1)
print(type(t1))  #<class 'numpy.ndarray'>


t2=np.array(range(1,10))
print(t2)

t3=np.arange(4,12,2)
print(t3)
print(t3.dtype)

#numpy 中的数据类型
t4=np.array(range(1,10),dtype=float)
t5=np.array(range(1,10),dtype="i1")
t6=np.array([0,1,0,0,1,0,1],dtype=bool)
print(t6)
#指定数据按照某一种数据类型输出
print(t6.astype("i1"))

#numpy中的小数
t7=np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

t8=np.round(t7,3)
print(t8)

np.loadtxt