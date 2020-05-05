# coding=utf-8
from matplotlib import pyplot as plt


#figure 是图形图标的意思，这里只我们画的图
#通过实例化一个figure并且传递参数，能够在后台自动使用该figure实例
#在图像木户的时候，可以传入dpi参数，让图片更清晰

fig=plt.figure(figsize=(20,8),dpi=80)
#数据在x轴的位置，是一个可迭代对象
x=range(2,26,2)

y=[15,13,14.5,17,20,25,26,26,24,22,18,15]
plt.plot(x,y)

#设置x的刻度
plt.xticks(range(2,25,1))
plt.yticks(range(min(y),max(y)+1))

# 保存图片到位置，可以保存为svg这种给矢量图。方法不会有锯齿
plt.savefig("./t1.png")
plt.show()


