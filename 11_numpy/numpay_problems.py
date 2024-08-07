import numpy as np

lst1=[1,2,3,4,5]
lst2=[2,3,4,5,6]
lst3=[3,4,5,6,7]

arr1=np.array([lst1,lst2,lst3])
arr1=arr1.reshape(5,3)
print(arr1)