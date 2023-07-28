# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:40:05 2023

@author: Marko
"""

import numpy as np
# дискретна різниця [1,2,3,4]= [2-1,3-2,4-3] = [1,1,1]
arr = np.array([10,15,25,5])
newarr = np.diff(arr)
print(newarr)
# двічі обчислити дискретну різницю над масивом
newarr = np.diff(arr, n=2)
print(newarr)