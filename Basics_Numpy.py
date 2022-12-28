

"""list_1=[1,2,3,4]
list_2=[5,6,7,8]
print(list_1*list_2)"""

import numpy as np
"""numpy_1=np.array([1,2,3,4.6])# when you give one float value then the numpy_1 datatype bytes will change to float
numpy_2=np.array([5,6,7,8])
print(numpy_1.dtype)
print(numpy_1.itemsize)# it will give datatype size like for int :4,  float:8
print(numpy_1*numpy_2)"""

"""#for exact value in array we will give the dtype='flaot64'

#array_2=np.array(([[1,2,3],[1,2,3,]], [[4,5,6],[5,6,7]],[[4,5,6],[5,6,7]]))
#array_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(array_2d)
array_2=np.array([[1,2,3,4,5,6],[5,6,7,8,9,2]])
array_2[0,2]=10 #it will change the value in array_2 of zero index of second value
#print(array_2[:,2])#indexing in 2d matrix
#print(array_2[1:,-2])
#for steping step-,start:end:stepsize
print(array_2[:,0:5:2])
#print("Dimensions{}".format(array_2.ndim))
#print("shape{}".format(array_2.shape))"""


"""array_2=np.array([[[1,2,3,4],[1,2,3,4]], [[4,5,6,6],[5,6,7,6]],[[4,5,6,7],[5,6,7,7]]])
print(array_2)
print(array_2.shape)
print(array_2[0,0,2])
print(array_2 [1,1,2])
#array_2[:,0,:]=[[20,10,30,40],[10,20,40,50]]"""#to replace  the values in 3d array

#print(np.zeros([2,3],dtype="int32"))
#print(np.zeros([2,3,3]))
#print(np.full([2,3,3],[11,12,13]))


#array_1=[1,2,3]
#print(np.full_like(array_1,[4,5,6]))

#for repeat
"""array_2=[[1,2,3],[4,5,6]]
array_repeat=np.repeat(array_2,2,axis=1)
print(array_repeat)"""

# for inserting the values in particular row and columns
"""a= np.zeros([3,3])
a[1,1]=7
#print(a)

updated_array=np.zeros([5,5])
updated_array[1:-1,1:-1]=a
print(updated_array)"""

#math operations
"""raki=np.array([1,2,3])
print(np.sin(raki+10))
print(np.sinh(raki+10))"""

"""a=np.ones([2,3])
b_1=np.full([3,2],4)
#print(a*b_1)
print(np.matmul(a,b_1))"""

"""array_2=([1,4,3],[4,5,10])
print(np.max(array_2))
print(np.max(array_2,axis=0))# in axis=0 it will take element by element and print the max element
print(np.max(array_2,axis=1))# in axis=1 it will take whole set and print the max element in the set"""

""""#arange will give the numbers it is like range(start,stop,increment or step)
raki_1=np.arange(12).reshape([4,3])#reshape will reshape the elements
print(raki_1)

raki=np.array([[1,2,3,4,5,6,7,8],[9,10,11,2,3,4,56,78]]).reshape([4,4])

print(raki)"""

"""def raki_1(x,y,z,r):
    return 10*x+y+z+r

b=np.fromfunction(raki_1,(2,3,3,2))
print(b)"""

"""data_from_text=np.genfromtxt('rakesh.txt',delimiter=',',dtype='int32')
print(data_from_text)
print(data_from_text.reshape([4,4]))
#data_from_text.astype('float64')
print(data_from_text[data_from_text<=0])"""

data=np.genfromtxt('rakesh.txt',delimiter=',',filling_values=10)
print(data)