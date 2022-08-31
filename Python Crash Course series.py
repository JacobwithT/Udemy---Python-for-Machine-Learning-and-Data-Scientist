import numpy as np
import seaborn
import matplotlib.pyplot

print(4 % 2)
print('My number is {one} and name is {two}'.format(one=6476290401,two='Jingbo')) # this is how you can format your print

s='hello'
print (s[0:4]) # you can grab the forth character of the S, in this case it is up to 4


my_list=['a','b','c','d']
my_list.append('u')
print(my_list)
my_list[0]='replacement value'
print(my_list)

# you can nest list as well
nest=list()
nest.append(my_list)
nest.append([1,2,3,4]) #---> you can nest two lists together
print(nest)

# if you want to grab the elements in the list
print(nest[1][0]) # use nested fields


#DICTIONARY
d={'key1':'1','key2':'2'}
print(d['key1'])

#How do I add a key to an existing dictionary? It doesn't have an . add() method. If you just use <dictionary>[<key>] = <value> and if the key doesn't exist, the key will be automatically added.

d={'k1':[1,2,3]} # you can add lists to your dictionary
d1 = {'klist':[1,2,3,4,5,6]}
print(d1['klist'])
# tuples are immutable, you can not reassign the values inside

set([1,2,3,4,5,6,6,7,7,7,8,8,6,4,5,4,4,5])#you can use the set to filter for unique elements

print( 1<2 and 2>3 ) # connecting the operator and
print(1<3 or 2>3) # connecting the operator by or



#if and then statement
if 1<2:
    print ('yep!')
else:
    print('you suck!')

# for loop

seq =[1,2,3,4,5]
for x in seq:
    print(x)   # the x is just a temporary variable

i=1
# while loop
while i<5:
    print('i is: {}'.format (i))
    i=i+1


for x in seq:
    print(x)
 # range object
for x in range (0,5):
    print(x)

my_list = (range(10)) # gives you a list of variables
out = []
x =[1,2,3,4]
for num in x:
    out.append(num**2)
print(out)

print([num**2 for num in x])## this the same thing as the for loop above

## define an function

def my_func(parm1):
    print('my name is' + parm1) ## pass in the parameter

print (my_func('my name'))


'''this is a doc sting. you can do this for multiple lines. this can serve as the documentation string'''
