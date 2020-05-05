"""
============
Scatter plot
============

This example showcases a simple histogram 直方图
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_properties = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
plt.figure(figsize=(20, 8), dpi=80)

a = ["战狼", "速度与激情", "公寓瑜伽", "西游伏魔篇", "变形金刚:最后的战士", "摔跤吧，爸爸", "加勒比海盗"]
b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8]

plt.bar(range(len(a)), b, width=0.3)
plt.xticks(range(len(a)), a, font_properties=font_properties)

plt.show()
