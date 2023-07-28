# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:34:22 2023

@author: Marko
"""

import numpy as np
# добуток елементів в масиві
arr = np.array([1,2,3,4])
x = np.prod(arr)
print(x)

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

x = np.prod([arr1,arr2])
print(x)
x = np.prod([arr1,arr2],axis=1)
print(x)

newarr = np.cumprod(arr2)
print(newarr)