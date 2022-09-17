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



fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(3,2)) #nice front handle to shortend the thing this is a axis manager
# the axes is a list object

axes[0].plot(x,y)
axes[1].plot(y,x)

# you can add the titles and axes names too.

plt.tight_layout()



# saving the picture:
fig.savefig('xyz.png',dpi=200)


'''adding legend'''
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y,label='FIG1')
ax.plot(y,x, label = 'FIG2')

# add legend
ax.legend(loc=0) # this is showing the label named in the previous section. and choose the best location


'''setting colors'''

fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y,color='green',linewidth=20, alpha=0.2,linestyle='-.',marker='o',markersize=20,markerfacecolor='yellow',markeredgewidth=3,markeredgecolor='green') # you can put Hexcode as well. alpha is the transparency
# marker is the marker for the datapoints

ax.set_xlim([0,1]) #take a list that sets the lowerbond and upperbound of our value
ax.set_ylim([0,2]) # set the y axis limit




'''practice'''

x = np.arange(0,100)
y = x*2
z = x**2
fig=plt.figure()
fig=fig.add_axes([0,0,1,1],label='ax')
fig.plot(x,y)



pic=plt.figure()
ax1=pic.add_axes([0,0,1,1])
ax2=pic.add_axes( [0.2,0.5,.4,.4])
ax1.plot(z)
ax1.set_xlim(20,22)
ax1.set_ylim(30,50)
ax2.plot(y)
ax2.set_xlim(20,22)
ax2.set_ylim(30,50)


# two plots

fig,axes=plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y,lw=2,color='blue')
axes[1].plot(y,x, lw=3,color='red',ls='-.')


plt.show()
