# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:09:06 2020

@author: woshi
"""


# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:57:18 2020

@author: woshi
"""


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

y=[57479,55570,55936,56850]
for i in range(6):
    y.append(random.randint(55000,58000))
plt.grid(axis='y', alpha=0.75)
plt.ylabel('')
plt.title("PACKET_OUT时间分布",fontproperties = 'FangSong',fontsize = 12)
#plt.ylabel('个数',fontproperties = 'FangSong')
plt.xlabel('PACKET_OUT耗时/us',fontproperties = 'FangSong')
#plt.ylim((0, len(ERR)/1000*30))
#plt.xlim((-25,25))
plt.hist(y, # 绘图数据
        bins = 3, # 指定直方图的条形数为20个
        color = 'steelblue', # 指定填充色
        edgecolor = 'k', # 指定直方图的边界色
        label = 'a' )# 为直方图呈现标签
def to_percent(y, position):
    return str( y*10) + '%'
formatter = FuncFormatter(to_percent)
plt.gca().yaxis.set_major_formatter(formatter)
print(len(y))
print(sum(y)/len(y))