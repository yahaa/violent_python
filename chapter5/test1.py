import pandas as pd
from pandas import DataFrame
import numpy as np
d = {'col1': 'foo', 'col2': 2, 'col3': pd.Series([1, 2, 3, 4, 55]), 'col4': 4}
df = DataFrame(np.random.rand(10, 5))

print df.corr()
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, np.nan])
print s

dates = pd.date_range('20170117', periods=10)
df = pd.DataFrame(np.random.rand(10, 4), index=dates, columns=list('ABCD'))
print df

df1 = pd.DataFrame(d)
print df1
print df1.dtypes
print df1.index
print df1.columns
