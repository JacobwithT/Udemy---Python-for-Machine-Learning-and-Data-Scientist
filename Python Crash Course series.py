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

print(my_func('my name'))


'''this is a doc sting. you can do this for multiple lines. this can serve as the documentation string
you can press command key and hoover to see more information'''

'''MAP AND FILTER FUNCTION'''
def times2 (var):
    return var *2

seq=[1,2,3,4,5]
'''you want to apply the times to seq elements '''

print(list(map(times2,seq)))
'''lambda expression'''
t=lambda var:var*2
print(t(5))
print(list(map(lambda x:x^2,seq)))

'''filter'''
print(list(filter(lambda num:num%2 ==0,seq))) #--> this returns only the even number, the lambda expression returns the true or false value

s='hello my name is Sam'
print( s.split()) #spliting the string
'''you can also split based on the the text '''
tweet='Go Sports! #Sports'
print(tweet.split('#'))

d.keys()#return the keys
d.values() # return the value

lst=[1,2,3]
lst.pop()
print(lst)

#if you want to check something is on the list or not--

print('x' in [1,2,3])

'''tuple unpacking'''
x=[(1,2),(3,4),(5,6)]

for (a,b) in x:
    print(a)


'''excersice '''

print(7**4)
print(list(s.split()))

print('the diameter of earth is {} kilometers'.format(12742))
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

def domain_get(var):
    return list(var.split('@'))[1]
print(domain_get('jingbo@outlook.com'))

def find_dogs(s):
    return 'dog' in list(s.split())

print(find_dogs('is dog here'))


'''count dogs '''
def countdog(st):
    count=0
    for x in st.lower().split():
        if x=='dog':
            count=count+1
        else: pass
    return count

print(countdog('dog dog dog'))
seq = ['soup','dog','salad','cat','great']
'''filter words that start with s'''
print(list(filter(lambda word: word[0]=='s',seq)))

def caught_speeding(speed,is_birthday):
    if is_birthday:
        speeding=speed-5
    else:
        speeding=speed
    if speeding>80:
        return 'big ticket'
    elif speeding>60:
        return 'smalll ticket'
    else:
        return 'No ticket'

print(caught_speeding(81,True))