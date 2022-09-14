import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())

print(df['col2'].unique) # finding the unique value in an array
print(df['col2'].nunique) # if you want to see how many unique values are there in the array
print(df['col2'].value_counts())# how many times the unique value appears. -
