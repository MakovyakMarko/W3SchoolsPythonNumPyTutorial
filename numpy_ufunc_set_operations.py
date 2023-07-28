# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:01:44 2023

@author: Marko
"""

import numpy as np

arr = np.array([1,1,1,2,3,4,5,5,6,7])
x = np.unique(arr)
print(x)

# знаходження об'єднання двох масивів
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])

newarr = np.union1d(arr1, arr2)
print(newarr)

# пошук перетину
# необов'язковий параметр assume_unique, при роботі
# з наборами має бути встановлений в True
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)

# знаходження різниці множини 1 від множини 2
set1 = np.array([1,2,3,4])
set2 = np.array([3,4,5,6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)

# знаходження симетричної різниці
set1 = np.array([1,2,3,4])
set2 = np.array([3,4,5,6])
newarr = np.setxor1d(set1,set2, assume_unique=True)
print(newarr)