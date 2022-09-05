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

arr=np.arange(0,11)
print(arr[8])
print(arr[1:5])


'''boardcasting values'''
arr[0:5]=100
print(arr)

''' if you slice the array and create a new one, 
the things you broadcasted in to the array is going to affect the original array as well'''
slice_of_arr=arr[0:6]
slice_of_arr[:]=99
print(arr)
'''if you dont want this to happen, you need to do this'''
slice_of_arr2 = arr[0:6].copy()
print(slice_of_arr2)

'''slicing a two dimensional array'''
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)

'''first row and first element in the row'''
print(arr_2d[0][0])

print (arr_2d[2][1])
#or you can do this
print(arr_2d[1,2])

'''slicing the array'''
print(arr_2d[:2,1:])# slice to 0 and 1 9not including 2 for the row, and including 1 all the way to the end for columns

'''conditional selection'''

arr=np.arange(1,11)
print(arr)
bool_arr=arr>5
'''you can use this boolean to select elements'''

print(arr[arr>5])

print(arr[arr<3])

arr_2d=np.arange(50).reshape(5,10)
print(arr_2d[1:3,3:5])

'''array with array'''

arr=np.arange(0,11)
print(arr+arr) # adding

print(arr+100)# every elements add 100

#taking square root
print(np.sqrt(arr))
print(np.max(arr))

'numpy excercise'
print(np.zeros(10))# print 10 zeros
print(np.ones(10))#pinrt 10 ones
print(np.ones(10)*5)

print(np.arange(10,51)) #to have 10 to 50 you have to include 51

print(np.arange(10,51,2))
print(np.arange(0,9).reshape(3,3))
#identity matrix

print(np.eye(3))

print(np.random.rand(1))
print(np.random.randn(25))# return 25 numbers in a normal distribution center in 0

print(np.linspace(0.01,1,100).reshape(10,10))
print(np.arange(0.01,1.01,0.01).reshape(10,10))

'''if you want the output into brackets instead of a single line of array '''
mat=np.arange(1,26).reshape(5,5)
print(mat[:3,1:2]) # you have to do this!


'''if you want to have the sum of all the value in array'''
print(np.sum(mat))
print(np.std(mat)) #--> getting standard deviation
print(mat.sum(axis=0)) #suming the first axis
