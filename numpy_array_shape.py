# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 16:21:46 2023

@author: Marko
"""

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)

arr = np.array([1,2,3,4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)