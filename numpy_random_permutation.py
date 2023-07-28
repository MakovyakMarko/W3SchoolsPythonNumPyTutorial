# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 11:38:12 2023

@author: Marko
"""

from numpy import random
import numpy as np

# shuffle вносить зміни в вихідний масив
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)

# permutation залишає вихідний масив без змін
arr = np.array([1,2,3,4,5])
print(random.permutation(arr))
