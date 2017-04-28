# -*- coding: UTF-8 -*-
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


dota = pd.read_csv('dota2Dataset/dota2Test.csv')
train = dota[0:20]
j, n_features = train.shape
df = DataFrame(train)

c = df.corr()
f, ax = plt.subplots(figsize=(10, 10))

mask = np.zeros_like(c, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(c, mask=mask, cmap=cmap, vmax=.3,
            square=True, xticklabels=5, yticklabels=2,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

sns.plt.show()
