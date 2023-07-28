# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:29:08 2023

@author: Marko
"""

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])

newarr = np.add(arr1,arr2)
print(newarr)

newarr = np.sum([arr1,arr2])
print(newarr)

newarr = np.sum([arr1,arr2], axis=1)
print(newarr)

# cumsum = [1,2,3,4] = [1,1+2,1+2+3,1+2+3+4] = [1,3,6,10]
arr = np.array([1,2,3,4])
arr = np.cumsum(arr)
print(arr)