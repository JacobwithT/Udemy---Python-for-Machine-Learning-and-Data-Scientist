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