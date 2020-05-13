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
x=[1577864553454237112 ,1577864553455547996 ,1577864553456832648 ,1577864553458153437 ,1577864553479086014 ,1577864553480401590 ,1577864553481725383 ,1577864553483035800 ,1577864553484343549 ,1577864553485662432 ,1577864553504911457 ,1577864553506233012 ,1577864553507551324 ,1577864553508857338 ,1577864553530920480 ,1577864553532209539 ,1577864553533551858 ,1577864553535185799 ,1577864553556922090 ,1577864553558281837 ,1577864553559521906 ,1577864553560813672 ,1577864553582889762 ,1577864553584176299 ,1577864553585465325]
print(len(x))
y=[]
for i in range(1,len(x)-1):
    y.append((x[i]-x[i-1])/1000)
print(y)
y.append(1320.789)
y.append(1320.789)
y=sorted(y)[:19]
plt.grid(axis='y', alpha=0.75)
plt.ylabel('')
plt.title("流表安装时间分布",fontproperties = 'FangSong',fontsize = 12)
#plt.ylabel('个数',fontproperties = 'FangSong')
plt.xlabel('安装耗时/us',fontproperties = 'FangSong')
#plt.ylim((0, len(ERR)/1000*30))
#plt.xlim((-25,25))
plt.hist(y, # 绘图数据
        bins = 5, # 指定直方图的条形数为20个
        color = 'steelblue', # 指定填充色
        edgecolor = 'k', # 指定直方图的边界色
        label = 'a' )# 为直方图呈现标签
def to_percent(y, position):
    return str( y*4) + '%'
formatter = FuncFormatter(to_percent)
plt.gca().yaxis.set_major_formatter(formatter)
print(len(y))
print(sum(y)/len(y))