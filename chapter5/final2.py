# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (precision_score, recall_score, f1_score)

# 准备数据
test_set = pd.read_csv('raw/TestSet.csv')
train_set = pd.read_csv('raw/TrainingSet.csv')

train = train_set.drop(
    ['EbayID', 'QuantitySold', 'SellerName', 'EndDay'], axis=1)
train_target = train_set['QuantitySold']

n_trainSamples, n_features = train.shape


# 画出训练过程中SGDClassifier利用不同的mini_batch学习的效果
def plot_learning(clf, title):

    plt.figure(figsize=(10, 6))
    # 记录上一次训练结果在本次batch上的预测情况
    validationScore = []
    # 记录加上本次batch训练结果后的预测情况
    trainScore = []
    # 最小训练批数
    mini_batch = 1000
    for idx in range(int(np.ceil(n_trainSamples / mini_batch))):
        i = idx * mini_batch
        j = min((idx + 1) * mini_batch, n_trainSamples)
        x_batch = train[i:j]
        y_batch = train_target[i:j]
        if idx > 0:
            validationScore.append(clf.score(x_batch, y_batch))
        clf.partial_fit(x_batch, y_batch, classes=range(5))
        if idx > 0:
            trainScore.append(clf.score(x_batch, y_batch))
    plt.plot(trainScore, label="train score")
    plt.plot(validationScore, label="validation socre")
    plt.xlabel("Mini_batch")
    plt.ylabel("Score")
    plt.legend(loc='best')
    plt.grid()
    plt.title(title)


# 对数据进行归一化
scaler = StandardScaler()
train = scaler.fit_transform(train)
# 创建SGDClassifier
clf = SGDClassifier(penalty='l2', alpha=0.001)
plot_learning(clf, "SGDClassifier")

plt.show()


test = test_set.drop(
    ['EbayID', 'QuantitySold', 'SellerName', 'EndDay'], axis=1)
test_target = test_set['QuantitySold']
test = scaler.fit_transform(test)
test_pre = clf.predict(test)

totest = len(test_target)
t1 = sum(test_target.values)
print t1
t2 = totest - t1
plt.pie([t1, t2], labels=['success', 'faild'], autopct='%1.2f%%')
plt.title('total ' + str(totest))
plt.show()


totest = len(test_pre)
t1 = sum(test_pre)
t2 = totest - t1
plt.pie([t1, t2], labels=['success', 'faild'], autopct='%1.2f%%')
plt.title('total ' + str(totest))
plt.show()


y = [0, precision_score(test_target, test_pre), recall_score(
    test_target, test_pre), f1_score(test_target, test_pre), 0]
x = [0, 1, 2, 3, 0]

plt.bar(x, y, 0.05, color='green')
plt.xticks((1, 2, 3), ('Precision', 'Recall', 'F1'))
plt.annotate(y[1], xy=(1, y[1]), xytext=(1, y[1]))
plt.annotate(y[2], xy=(2, y[2]), xytext=(2, y[2]))
plt.annotate(y[3], xy=(3, y[3]), xytext=(3, y[3]))
plt.ylabel('score')
plt.show()


print("SGDClassifier 训练测试结果如下:")
print("\tPrecision: %1.3f " % precision_score(test_target, test_pre))
print("\tRecall: %1.3f" % recall_score(test_target, test_pre))
print("\tF1: %1.3f \n" % f1_score(test_target, test_pre))
