import numpy as np

n=[6,7,8]
print("array :",n)
print("slicing an array : ",n[0:2])


#3d array
a=np.array([[2,3,4],[5,1,6],[7,1,2]])
print("3d array :",a)


#last row of array
print("last row in array :",a[-1])

#all rows acn be accessed
print("accessing rows using for loop\n")
for row in a:
    print(row)

b=np.arange(6,15).reshape(3,3)
print("array b :\n",b)


#merging two arrays vertically
print(" merging two arrays vertically :",np.vstack((a,b)))

#merging two arrays horizontally
print(" merging two arrays horizontally :",np.hstack((a,b)))