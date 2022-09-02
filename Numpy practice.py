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