import numpy as np

lst1=[1.234,2.098,3.970,4.673]
lst2=[2.567,4.192,6.872,8.98007]

arr1= np.array(lst1)
print(arr1)
print(type(arr1))

arr2= np.array(lst2)
print(arr2)
print(type(arr2))

print(np.concatenate((arr1,arr2)))
print(np.concatenate((arr1.reshape(len(arr1),1),arr2.reshape(len(arr2),1)),axis=1))
print(np.concatenate((arr1.reshape(len(arr1),1),arr2.reshape(len(arr2),1)),axis=0))
np.set_printoptions(precision=2)
print("\n\n")
print("precison printing")
print(np.concatenate((arr1.reshape(len(arr1),1),arr2.reshape(len(arr2),1)),axis=1))


# THIS METHOD PRINTS WHOLE ARRAY WITHOUT TRUNCATING IF WE HAVA TOO MUCH ELEMENTS(.. K JAGAH PURA VALUE SHOW KAREGA)
# import sys
# import numpy
# numpy.set_printoptions(threshold=sys.maxsize)
