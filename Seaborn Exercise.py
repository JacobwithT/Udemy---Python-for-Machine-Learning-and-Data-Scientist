import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')

titanic = sns.load_dataset('titanic')

#print(titanic.head())

#sns.jointplot(titanic,x='fare',y='age')
#sns.displot(titanic,x='fare',color='red')
#sns.displot(titanic['fare'],kde=False, color='pink')
#sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')
#sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')
#sns.countplot(titanic,x='sex')
#sns.heatmap(titanic.corr(),cmap='coolwarm') # this is the heatmap
g=sns.FacetGrid(titanic,col='sex') # creating a grid for plotting
g.map(plt.hist,'age')
 

plt.show()