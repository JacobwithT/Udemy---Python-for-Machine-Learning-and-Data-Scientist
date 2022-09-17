import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
tips = sns.load_dataset('tips')

print(tips)

'''One way to rule them all'''
#sns.factorplot(x='day',y='total_bill',data=tips,kind='violin')# call all kinds of plots using one command!

#sns.distplot(tips['total_bill'],bins=10) # say number of bins you want to display

sns.jointplot(x='total_bill',y='tip',data=tips, kind='hex') # joining the plot
'''Nice to haves'''
sns.pairplot(tips,hue='sex')
# it is the paring comparison for every single possible connection, just pass in the dataframe
# the hue is going to be categoricals

sns.rugplot(tips['total_bill'])

'''categorical data'''
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std) # bar plot x = categories estimator is the y scale
#sns.countplot() -- show the count only

sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker') # hue is added another layer
sns.violinplot(x='day',y='total_bill',data=tips, hue='sex', split=True)# you can split the plots by sex
sns.stripplot(x='day', y='total_bill',data=tips, jitter=True, hue='sex',split=True)# jitter will enable the the point split


'''combining swarmplot'''
sns.violinplot(x='day',y='total_bill',data=tips)
sns.swarmplot(x='day',y='total_bill',data=tips,color='black')

'''One way to rule them all'''
#sns.factorplot(x='day',y='total_bill',data=tips,kind='violin')# call all kinds of plots using one command!

flights=sns.load_dataset('flights')
'''in order for matrix to work, the dataset should already be in matrix form'''
tc=tips.corr()
sns.heatmap(tc)
plt.show()


fp=flights.pivot_table(index='month',columns='year',value='passengers')
sns.heatmap(fp,cmap='magma')