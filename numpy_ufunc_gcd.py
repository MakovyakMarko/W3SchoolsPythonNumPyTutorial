# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:48:18 2023

@author: Marko
"""

# найбльший спільний множник (знаменник)
import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1, num2)
print(x)

arr = np.array([20,8,32,36,16])
x = np.gcd.reduce(arr)
print(x)