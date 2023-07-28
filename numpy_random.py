# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 02:35:54 2023

@author: Marko
"""

from numpy import random
# випадкове число
x = random.randint(100)
print(x)
# випадкове плаваюче значення (від 0 до 1)
x = random.rand()
print(x)
# генерація випадкового масиву
x = random.randint(100, size = (5))
print(x)
# випадковий 2д масив
x = random.randint(100, size = (3,5))
print(x)
# масив плаваючих значень
x = random.rand(5)
print(x)
# 2д масив плаваючих значень
x = random.rand(3,5)
print(x)
# генерація випадкових чисел з масиву
x = random.choice([3,5,7,9])
print(x)
# choise масив
x = random.choice([3,5,7,9], size =(3,5))
print(x)