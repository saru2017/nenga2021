#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://rhinohattan.com/matplotlibで連続的に変化するcmapを作成/

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# cmap作成
colors = ['#000000','#EA930A']
#colors = ['#0080ff','#00d5ff','#00ffd5','#00ff80',
#          '#00ff2b','#2bff00','#80ff00','#d5ff00',
#          '#ffd500','#ff8000','#ff2000']
cmap = LinearSegmentedColormap.from_list('custom',colors)
print(cmap)
# データ作成
x = [1,2,3,4,5]
y = [1,2,3,4,5]
X, Y = np.meshgrid(x,y)
Z = X 

# グラフ作成
fig = plt.figure()
ax = fig.add_subplot(111)
ax.contourf(X,Y,Z,levels=300,cmap=cmap)
plt.show()


