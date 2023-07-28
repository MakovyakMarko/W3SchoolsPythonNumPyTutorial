# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:50:14 2023

@author: Marko
"""

import numpy as np
arr1 = np.array([10,11,12,13,14,15])
arr2 = np.array([20,21,22,23,24,25])

newarr = np.add(arr1,arr2)
print(newarr)

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([20,21,22,23,24,25])

newarr = np.subtract(arr1,arr2)
print(newarr)

newarr = np.multiply(arr1,arr2)
print(newarr)

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([3,5,10,8,2,33])

newarr = np.divide(arr1,arr2)
print(newarr)

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([3,5,6,8,2,33])

newarr = np.power(arr1,arr2)
print(newarr)

# mod = %
arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([3,7,9,8,2,33])

newarr= np.mod(arr1,arr2)
print(newarr)

newarr = np.remainder(arr1,arr2)
print(newarr)

# divmod = [a//b], [a%b]

newarr = np.divmod(arr1,arr2)
print(newarr)

# absolute = |x|
arr = np.array([-1,-2,1,2,3,-4])

newarr = np.absolute(arr)
print(newarr)