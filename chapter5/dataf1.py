import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


testSet = pd.read_csv('raw/TestSet.csv')
trainSet = pd.read_csv('raw/TrainingSet.csv')
testSubSet = pd.read_csv('raw/TestSubset.csv')
trainSubSet = pd.read_csv('raw/TrainingSubset.csv')



print testSet

train = trainSet.drop(['EbayID', 'QuantitySold', 'SellerName','EndDay'], axis=1)
trainTarget = trainSet['QuantitySold']

print train

xx, nfeatures = train.shape
df = DataFrame(train, trainTarget[:, None], columns=range(
    nfeatures) + ['isSold'])
xx = sns.pairplot(df[:50], vars=[2, 3, 4, 10, 13], hue='isSold', size=1.5)
plt.figure(figsize=(10, 10))
corr = df.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, square=True,
            xticklabels=5, yticklabels=2, linewidths=.5, cbar_kws={"shrink": .5})
plt.yticks(rotation=0)
plt.show()

