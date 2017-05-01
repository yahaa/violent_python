# coding:utf8

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c = np.cos(x)
s = np.sin(x)
plt.figure(figsize=(10, 6), dpi=80)
plt.plot(x, c, 'r-', lw=3.5,label='cos')
plt.plot(x, s,label='sin')
plt.xlim(x.min() * 1.1, x.max() * 1.1)
plt.ylim(c.min() * 1.1, c.max() * 1.1)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$',  r'$0$', r'$\pi/2$', r'$+\pi$'])
plt.legend(loc='upper right')

plt.show()
