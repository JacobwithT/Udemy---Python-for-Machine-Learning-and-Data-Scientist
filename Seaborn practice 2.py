import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
'''

flights=sns.load_dataset('flights')
fp=flights.pivot_table(index='month',columns='year',values='passengers')
sns.clustermap(fp,cmap='coolwarm',standard_scale=1)
'''
tips = sns.load_dataset('tips')


iris = sns.load_dataset('iris')
''''
ploting=sns.PairGrid(iris) # DIY version of the pairplot
# you dont need the parentheses
ploting.map(sns.displot)
ploting.map(sns.scatterplot)
ploting.map(sns.violinplot)
'''


g=sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(sns.scatterplot,'total_bill','tip')

'''REGRESSION PLOTS'''
sns.lmplot(x='total_bill', y='tip',data=tips, hue='sex',markers=['o','v'],scatter_kws={'s':50}) # linear regression --> color seperated by sex this plot has matplot lib embeded
sns.lmplot(x='total_bill', y='tip',data=tips, col='sex',palette='seismic')

'''STYLE AND COLOR'''

sns.set_style('ticks')
sns.set_context('poster') # set the contaxt for our plot - make it bigger or smaller
sns.countplot(x='sex',data=tips)
sns.despine()# remove the spines you can remove four sides
plt.figure(figsize =(12,3)) # you can set the size for you plot
sns.set_context('poster')






plt.show()
