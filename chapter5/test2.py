import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data=pd.read_csv('raw/TestSet.csv')
train=data.drop(['EbayID', 'QuantitySold', 'SellerName'],axis=1)
sns.heatmap(train)
plt.show()