"""
============
Scatter plot
============

This example showcases a simple scatter plot. 散点图
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

# Fixing random state for reproducibility
np.random.seed(19680801)

font_properties = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
N = 30
x_1 = range(1, 31)
x_2 = range(51, 81)
y_1 = np.random.rand(N)
y_2 = np.random.rand(N)
colors = np.random.rand(N)
area = (5 * np.random.rand(N)) ** 2  # 0 to 15 point radii

plt.scatter(x_1, y_1, s=area, c=colors, alpha=0.5, label="3月份")
plt.scatter(x_2, y_2, s=area, c=colors, alpha=0.5, label="10月份")

# 调整x轴的刻度
_x = list(x_1) + list(x_2)
_xtick_labels = ["3月{}日".format(i) for i in x_1]
_xtick_labels += ["10月{}日".format(i - 50) for i in x_2]
plt.xticks(list(_x)[::5], list(_xtick_labels)[::5], rotation=45, font_properties=font_properties)

# 添加描述信息
plt.xlabel("时间", font_properties=font_properties)
plt.ylabel("温度 单位(℃)", font_properties=font_properties)
plt.title("3月和10月温度比较", font_properties=font_properties)

# 添加图例
plt.legend(prop=font_properties,loc="upper left")

plt.show()

#############################################################################
#
# ------------
#
# References
# """"""""""
#
# The use of the following functions and methods is shown in this example:
import matplotlib

matplotlib.axes.Axes.scatter
matplotlib.pyplot.scatter
