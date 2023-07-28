# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 02:45:58 2023

@author: Marko
"""

from numpy import random
# p - ймовірність появи числа в масиві, сума ймовірностей 
# повинна бути рівна 1
x = random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(100))
print(x)
# 2d масив з троьох масивів по 5 значень
x = random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(3,5))
print(x)



