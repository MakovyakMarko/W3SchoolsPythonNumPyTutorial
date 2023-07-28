# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 14:14:24 2023

@author: Marko
"""

import numpy as np 
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr, 3)
print(newarr)

newarr = np.array_split(arr, 4)
print(newarr)

newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
newarr = np.array_split(arr,3)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr,3)
print(newarr)

newarr = np.array_split(arr,3, axis=1)
print(newarr)


newarr = np.hsplit(arr,3)
print(newarr)

newarr = np.vsplit(arr,3)
print(newarr)
