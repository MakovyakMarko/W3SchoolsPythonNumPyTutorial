# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 16:07:22 2023

@author: Marko
"""

import numpy as np

arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

arr = np.array([1,2,3,4,5])
x = arr.view()
x[0] = 31
print(arr)
print(x)

arr = np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)