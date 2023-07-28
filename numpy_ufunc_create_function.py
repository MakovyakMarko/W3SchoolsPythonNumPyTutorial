# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:40:36 2023

@author: Marko
"""

import numpy as np

def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1,2,3,4],[5,6,7,8]))

print(type(np.add))
print(type(np.concatenate))

if type(np.add) == np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')