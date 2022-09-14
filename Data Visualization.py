import numpy as np
import matplotlib.pyplot as plt

'''
matplotlib.org this is the website that you can explote the charts that is available in Matplotlib
'''
x=np.linspace(0,5,11)
y=x**2

# functional method

plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('This is the title')


'''creating multi-plot'''

plt.subplot(1,2,1) #num of rows, num of columns, and number of plot number
plt.plot(x,y,'r')
plt.subplot(1,2,2) # this is the second graph that we will run
plt.plot(y,x,'b')
#plt.show()



'''Object orientagted method- create a figure that is empty and then you pass in the values.'''

fig=plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8,]) # left of the axes, bottom of the axes, and width and height
axes2=fig.add_axes([0.2,0.5,0.4,0.3]) # the percentage of the things that from the bottom left corner

axes1.plot(x,y)
axes2.plot(y,x)
axes1.set_xlabel('X Label')
axes1.set_ylabel('Y Label')
axes1.set_title('Set Title')
axes2.set_xlabel('X Label')
axes2.set_ylabel('Y Label')
axes2.set_title('Larger Set Title')
plt.show()

