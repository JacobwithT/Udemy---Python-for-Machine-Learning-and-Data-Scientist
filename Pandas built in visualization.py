import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('/Users/jingbochen/Downloads/Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df1',index_col=0) # timeseries
df2 = pd.read_csv('/Users/jingbochen/Downloads/Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df2')
df3 = pd.read_csv('/Users/jingbochen/Downloads/Refactored_Py_DS_ML_Bootcamp-master/07-Pandas-Built-in-Data-Viz/df3',index_col=0)

df1['A'].hist(bins=30) # matplot under the hood
#df1["A"].plot(kind='hist',bin=30)
df1["A"].plot.hist()

df2.plot.bar(stacked=True)
#df1.plot.line(x=df1.index,y='B')
df1.plot.scatter(x='A',y='B',c='C',s=df1['C'])

'''By Variant'''

df=pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])
df.plot.hexbin(x='a',y='b',gridsize=25) # the more column in a hex, the darker it gets
df2.plot.density() #kernal desity plot for every column

plt.show()
