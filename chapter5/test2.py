# coding:utf8

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
data = pd.read_csv('raw/TestSet.csv')
train = data.drop(['EbayID', 'QuantitySold', 'SellerName', 'EndDay'], axis=1)
day = data['EndDay']
day = pd.DataFrame(day)
train['EndDay'] = day['EndDay'].replace(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], [1, 2, 3, 4, 5, 6, 7])

train_target = data['QuantitySold']
m, n = train.shape
df = pd.DataFrame(
    np.hstack((train, train_target[:, None])), columns=range(n) + ['IsSold'])

sns.pairplot(df[:100], vars=[3,8,11,15,22], hue='IsSold', size=1)
sns.plt.show()
