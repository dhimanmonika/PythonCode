import numpy as np

# numpy will be fast and take less memory as compared to python arrays
#creating array using numpy

a=np.array([1,2,3,4,5])
print("numpy array :",a)

#2D array
b=np.array([[1,2],[3,4],[5,6]])
print("numpy 2d array :",b)


#get dimensions of  array
print("dimenions of array a:",a.ndim)
print("dimenions of array b:",b.ndim)


#to get rows and cols
print("rows and cols in array b:",b.shape)

#make array with all zeros
c=np.zeros((3,4))
print(" array with all zeros\n",c)


#create array in range
d=np.arange(1,5)
print("array in range :",d)

# array in range with steps

d=np.arange(1,5,2)
print("array in range with steps:",d)

# divide  range between equal parts
d=np.linspace(1,10,5)
print("the range 1 to 10 in 5 equal spaces inbetween :\n",d)





