# -*- coding: UTF-8 -*-
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import DataFrame


def myPCA(dataMat, topNfeat=9999999):
    meanVals = np.mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals
    covMat = np.cov(meanRemoved, rowvar=0)
    eigVals, eigVects = np.linalg.eig(np.mat(covMat))
    eigValInd = np.argsort(eigVals)  # 对特征值进行从小到大的排列
    eigValInd = eigValInd[:-(topNfeat + 1):-1]
    redEigVects = eigVects[:, eigValInd]
    lowDDataMat = meanRemoved * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat


trainData = pd.read_csv('raw/TestSet.csv')
testData = pd.read_csv('raw/TrainingSet.csv')


train = trainData.drop(
    ['EbayID', 'QuantitySold', 'SellerName', 'EndDay'], axis=1)
test = testData.drop(
    ['EbayID', 'QuantitySold', 'SellerName', 'EndDay'], axis=1)


pca = PCA(n_components=5)


train = DataFrame(train)
test = DataFrame(test)

myPCAdata = myPCA(train.values, 5)
myPCAtest = myPCA(test.values, 5)


pcax = pca.fit_transform(train)
pcatest = pca.fit_transform(test)


trainTarget = trainData['Price']
testTarget = testData['Price']

# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=10)
regr_2 = DecisionTreeRegressor(max_depth=10)
regr_3 = DecisionTreeRegressor(max_depth=10)
regr_1.fit(pcax, trainTarget)
regr_2.fit(train, trainTarget)
regr_3.fit(myPCAdata, trainTarget)

y_1 = regr_1.predict(pcatest)
y_2 = regr_2.predict(test)
y_3 = regr_3.predict(myPCAtest)


# Plot the results
n = len(testTarget)
x = range(1, n + 1)

y_0 = list(testTarget)
plt.figure()
plt.xlim(0, 11)
axes = plt.subplot(111)
print '真实值：', y_0[:10]
print 'pca ：', y_1[:10]
print 'not_pca:', y_2[:10]
print 'myPCA :', y_3[:10]

t1 = axes.scatter(x[:10], y_0[:10], s=40, c='red')
t2 = axes.scatter(x[:10], y_1[:10], s=40, c='green')
t3 = axes.scatter(x[:10], y_2[:10], s=40, c='blue')
t4 = axes.scatter(x[:10], y_3[:10], s=40, c='yellow')

axes.legend((t1, t2, t3, t4), ('true', 'pca',
                               'no_pca', 'myPCA'), loc='upper left')
plt.xlabel("no")
plt.ylabel("price")
plt.title("compare")
plt.show()

plt.bar([i + 0.2 for i in x[:10]], y_0[:10],
        0.2, color='red', label='sample value')
plt.bar([i + 0.4 for i in x[:10]], y_1[:10],
        0.2, color='green', label='pca_predict')
plt.bar([i + 0.6 for i in x[:10]], y_2[:10], 0.2,
        color='blue', label='no_pca_predict')
plt.legend(loc='best')
plt.xlabel("sample_no")
plt.ylabel("Price")
plt.title("tree depth=10")
plt.show()
