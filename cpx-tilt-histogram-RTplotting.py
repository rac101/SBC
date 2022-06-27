#!/Users/rac/opt/anaconda3/bin/python

# Real Time Dynamic Plotting Testing
# Robert Cameron, May 2020

#import random
#from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#from matplotlib.ticker import MaxNLocator
#from matplotlib.ticker import AutoMinorLocator

plt.rcParams["figure.figsize"] = (10,6)
plt.rcParams["font.size"] = 15
#fig, ax = plt.subplots()
#ax.xaxis.grid(True, which='minor')
#ax.xaxis.set_minor_locator(AutoMinorLocator())
#ax.xaxis.set_major_locator(MaxNLocator(9)) 
plt.figure(num='CPX tilt histogram');

xpha = range(10)
xbins = range(11)
#plt.style.use('fivethirtyeight')

#x_vals = []
#y_vals = []

#index = count()

def animate(i):
#    data = pd.read_csv('data.csv')
    data = pd.read_csv('accel.csv',header=None)
#    yh = data.hist()
#    x = data['x_value']
###    y1 = data['total_1']
    y1 = data[0]
    lv = y1.iloc[-1]
#    lv = y1.iloc[-1]

    counts, edges = np.histogram(y1, bins=10,range=(0,10))
    m = max(counts)
    ym = m + (40 - m%10)
#    print(counts,lv,edges)

    plt.cla()
    plt.ylim(0,ym)
#    plt.xlabel('CPX tilt')
#    plt.ylabel('Number of Hits')
    plt.bar(xpha,counts)
#    plt.hist(y1,bins=xbins,rwidth=0.95)
    plt.text(4,ym*0.62, lv, fontsize=160)
#    plt.hist(y1)
#    plt.bar(yh)
#    plt.plot(x, y1, label='Channel 1')
#    plt.plot(x, y2, label='Channel 2')

#    plt.legend(loc='upper left')
#    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

#plt.tight_layout()
#plt.xticks(np.arange(-1, 11, step=1))  # Set xtick labels
plt.show()
