import pandas as pd
import numpy as np

'''series'''
#series have labels that is different from numpy arrays

labels=['a','b','c']
my_data = [10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}
print(pd.Series(data=my_data))

#assigning labels
print(pd.Series(data=my_data,index=labels)) # --> assign the index

print(pd.Series(arr,labels)) # you can also pass in numpy array and specify the index
print(pd.Series(d)) # if you pass dictionary, then the keyward is just become index

ser1=pd.Series([1,2,3,4],['USA','Germany','USSR','Japan']) # a series can take any objects
ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])

print(ser1['USA']) # passing the index and get the value
print(ser1[1])# you can return the index position as well


# you can add two panda series together, it will sum if the inexes are matches and NaN if they are not a match

print(ser1+ser2) # the integers are going to be converted in to float



'''data framework '''

from numpy.random import randn

np.random.seed(101) # locking the data seed
df=pd.DataFrame(randn(5,4),['a','b','c','d','e'],['W','X','Y','Z'])
'''this is a bunch of pandas series with shared indexes '''
print(df)

'''grabbing information in df'''

print(df[['W','Z']]) # grabbing column W or you can do df.w --> the same thing. you can do multiple columns too

df['new']=np.array( randn(5)) # the dataframe can only take np arrays
df.drop('new',axis=1) #--> drop the column
df.drop('new',axis=1,inplace =True)
print(df)


# selecting rows

 # or if you want to use index location use df.iloc

#selecting multiple rows
print(df.loc[['a','b']]) # you need to use double []
# selecting a sub frame:

print(df.loc[['a','b'],['W','Y']])# row a,b and column W Y


# conditional selection
booldf=df>0 # creating a boolean dataframe

print(df[df>0].dropna(axis=1))# axis =1 is dropping by rows

#passing multiple conditions

''' you need to use & notation instead of and'''
'''you need to use | notation instead of or'''
print(df[(df['W']>0) & (df['Y']>0)])

#reseting the index
print(df.reset_index())# this will return the index to a column

new_ind='CA NY WY OR CA'.split()
df['States']=new_ind
df.set_index('States',inplace=True)
print(df)


# multilevel index
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index) #creating a multilevel index

df=pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)


# calling from multi level index
print(df.loc['G1'].loc[1]) # call from the outside to inside


# you can name your multi index levels
df.index.names=['Groups','Num']# now your dataframe has titles under each columns
print(df)

print(df.xs(1,level='Num'))# cross section. grabbing every row named 1 when the level is Num


'''Missing Data'''

d={'a':[1,2,np.nan],'b':[5,np.nan,np.nan],'c':[1,2,3],}
df=pd.DataFrame(d) # creating dataframe from dictionary
df.dropna(thresh=2,inplace=True) #axis=1 is dropping columns,thresh is the number of NA needed to be droped
print(df)

#fill na
df.fillna(value=df.mean(),inplace = True) # filling the NA with mean of the dataset
print(df)


'''Group BY'''

import pandas as pd
# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df=pd.DataFrame(data)
print(df)

bycomp=df.groupby('Company')
print(bycomp.sum())# group by and perform the average of the columns

#you can call the sum and call the sepecific value

print(bycomp.sum().loc['FB'])

# say you want to grab the sum of facebook:

df.groupby('Company').sum().loc['FB']

# call a number of columns.
print(df.groupby('Company').describe().transpose())


'''Merging, joining, and concatenating'''

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

print(df1)
print(df2)
print(df3)


#concatenate the three dataframes above

df_concate_column=pd.concat([df1,df2,df3])
print(df_concate_column)

df_concate_row = pd.concat([df1,df2,df3],axis=1)
print(df_concate_row)

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

df_merge=pd.merge(left,right,how='inner',on = 'key') # on is the primary key, you can select multiple primary keys

#joining


left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

df_join=left.join(right) # joining the dataframes

print(df_join)

'''operations'''

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())

print(df['col2'].unique) # finding the unique value in an array
print(df['col2'].nunique) # if you want to see how many unique values are there in the array
print(df['col2'].value_counts())# how many times the unique value appears. -

# conditional selection

def time2(x):
    return x*2

print(df['col1'].apply(time2)) # this will broadcast the function into the column

print(df['col2'].apply(lambda x: x*2)) # take lambda expression

#remove columns
df.drop('col1',axis=1,inplace = True)

# sorting and ordering
#sort by column 2

print(df.sort_values('col2')) # sort by column 2


data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)

print(df.pivot_table(values='D', index=['A','B'],columns=['C'])) # take three values,
# whenever you pass the index that is more than 2, then you should pass it on as a list

'''Data input and output'''

'''CSV'''
#df=pd.read_csv()
#df.to_csv('filepath', index=False) # indicating if you want to save the index

'''Excel'''
df=pd.read_excel('/Users/jingbochen/Downloads/Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/Excel_Sample.xlsx',sheet_name='Sheet1')
# you can pass in the sheet name as you go along
print(df)
'''HTML'''

#df_html = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
#print(df_html[0].head())

'''SQL'''
from sqlalchemy import create_engine
engine=create_engine('sqlite:///:memory:')
df.to_sql('my_table',engine) # the engine is the connector

sqldf=pd.read_sql('my_table',con=engine)
print(sqldf)


salaries=pd.read_csv('/Users/jingbochen/Downloads/Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises/Salaries.csv')

print(salaries.head())

print(salaries.groupby('Year').mean())
print(salaries['EmployeeName'].value_counts().head(5))

Ecommerce=pd.read_csv('/Users/jingbochen/Downloads/Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises/Ecommerce Purchases')
print(Ecommerce)
print(Ecommerce[Ecommerce['Language']=='en'].count())


print(Ecommerce['AM or PM'].value_counts())
print(Ecommerce['Job'].value_counts().head(5))
print(Ecommerce['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))