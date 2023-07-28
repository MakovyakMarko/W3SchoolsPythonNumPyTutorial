# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:22:52 2023

@author: Marko
"""

import numpy as np

arr = np.arange(1,10)

print(np.log2(arr))
print(np.log10(arr))
print(np.log(arr))

from math import log

nplog = np.frompyfunc(log, 2,1)
print(nplog(100,15))