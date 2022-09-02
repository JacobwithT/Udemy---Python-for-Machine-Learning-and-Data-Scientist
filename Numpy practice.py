import numpy as np

'''this can be 1D or 2D arrays'''
my_list=[1,2,3]
print(np.array(my_list))

my_mat=[[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_mat))

'''building an array range'''
print(np.arange(0,11,0.1))# --> the third option is the step size

#if you want to have a range of zeros
print(np.zeros((5,5))) #--> returns 5 row by 5 columns table of zeros

'''linspace'''
print(np.linspace(0,5,10))# returns one diamensional array with evenly spaced list

'''creating a identity matrix'''

print(np.eye(4))

'''creating random numbers'''

print(np.random.rand(5))#--> you want 5 elements in one list that will have random numbers

print(np.random.rand(5,5)) # --> dimentional matrixs that will have 5 by 5 random numbers populated

'''random distribution that will have numbers have a uniform distribution centered around 0'''

print(np.random.randn(2,2)) # you can print 2 dimensional matrix too.

print(np.random.randint(1,100)) # one integer between 1 and 99 (100 is not included)

ranarr = np.random.randint(1,50,25)# return 10 integers between 1 and 50
print(ranarr.reshape(5,5)) #reshap the array to 5 X 5

print(ranarr.max(),ranarr.min())

'''if you want to know where is the max/ min value is located'''

print(ranarr.argmax()) # --> returning the max value index location
'''if you want to know the shape of the array'''

print(ranarr.shape) # return the shape of the array

'''return the data type inside your array'''

lst=np.array(['good',2,2,3.3])

print(lst.dtype)


