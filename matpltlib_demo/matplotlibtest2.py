# coding=utf-8
import random

from matplotlib import pyplot as plt
from matplotlib import font_manager

# windows/linux可以修改
# font = {'family': 'monospace',
#        'weight': 'bold',
#        'size': 'larger'}
# matplotlib.rc("font",**font)
# 展示出10点到12点每一分钟的气温
font_properties = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")

# figure 是图形图标的意思，这里只我们画的图
# 通过实例化一个figure并且传递参数，能够在后台自动使用该figure实例
# 在图像木户的时候，可以传入dpi参数，让图片更清晰

fig = plt.figure(figsize=(20, 8), dpi=80)
# 数据在x轴的位置，是一个可迭代对象
x = range(0, (12 - 10) * 60)

y = [random.randint(20, 25) for i in range(120)]
plt.plot(x, y)

# 调整x轴的刻度：创建和x 一一对应的字符串
_x = x

# x 太密集的时候可以设置步长
# _x2=list(x)[::10]
# _xtick_tables=["hello,{}".format(i) for i in _x2]
_xtick_tables1 = ["10点{}分".format(i) for i in range(60)]
_xtick_tables1 += ["11点{}分".format(i) for i in range(60)]

# 双步长，数字和字符串一一对应，数据的长度一致  rotation:旋转角度
plt.xticks(list(x)[::3], _xtick_tables1[::3], rotation=45, font_properties=font_properties)
# 设置x的刻度
# plt.xticks(range(2,25,1))
# plt.yticks(range(min(y),max(y)+1))

# 添加描述信息
plt.xlabel("时间", font_properties=font_properties)
plt.ylabel("温度 单位(℃)", font_properties=font_properties)
plt.title("10点到12点每分钟气温变化", font_properties=font_properties)

#设置网格
plt.grid(alpha=0.4)
# 保存图片到位置，可以保存为svg这种给矢量图。方法不会有锯齿
plt.savefig("./t2.png")

plt.show()
