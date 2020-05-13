# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:00:17 2020

@author: woshi
"""
import matplotlib
import matplotlib.pyplot as plt
import random
from matplotlib.ticker import FuncFormatter
matplotlib.rcParams.update(
    {
        'text.usetex': False,
        'font.family': 'stixgeneral',
        'mathtext.fontset': 'stix',
    }
)
y=[981457,
5107729,
5275524,
4603875,
3934335,
3306503,
2749802,
2167436,
1578564,
1017644,
5458027,
4892970,
4331197,
3762996,
3187320,
2630170,
2053515,
1489853,
925275,
5386829,
4817825,
4254171,
3698156,
3124951,
2566806,
1986830,
1426813,
860310,
5280343,
4717100,
4153746
]
# for u in range(1,50):
#     y.append(random.randint(2053515,4717100))
# for u in range(1,20):
#     y.append(random.randint(2853515,3853515))
plt.grid(axis='y', alpha=0.75)
plt.ylabel('')
plt.title("表项安装时间分布",fontproperties = 'FangSong',fontsize = 12)
#plt.ylabel('个数',fontproperties = 'FangSong')
plt.xlabel('安装耗时/ns',fontproperties = 'FangSong')
#plt.ylim((0, len(ERR)/1000*30))
#plt.xlim((-25,25))
plt.hist(y, # 绘图数据
        bins = 5, # 指定直方图的条形数为20个
        color = 'steelblue', # 指定填充色
        edgecolor = 'k', # 指定直方图的边界色
        label = 'a' )# 为直方图呈现标签
def to_percent(y, position):
    return str( y*2) + '%'
formatter = FuncFormatter(to_percent)
plt.gca().yaxis.set_major_formatter(formatter)
print(len(y))
print(sum(y)/len(y))