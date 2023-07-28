# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 14:00:52 2023

@author: Marko
"""

import numpy as np
arr = np.trunc([-3.1666, 3.6667])
print(arr)

arr = np.fix([-3.1666, 3.6667])
print(arr)

arr = np.around(3.1666,2)
print(arr)

arr = np.floor([-3.1666, 3.6667])
print(arr)

arr = np.ceil([-3.1666, 3.6667])
print(arr)
