# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:33:10 2023

@author: Marko
"""

# ufunc - означає "універсальна функція"


x = [1,2,3,4]
y = [4,5,6,7]
z = []
for i,j in zip(x, y):
    z.append(i+j)
print(x)

import numpy as np

z = np.add(x,y)
print(z)