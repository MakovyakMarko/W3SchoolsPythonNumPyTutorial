# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 11:48:23 2023

@author: Marko
"""

from numpy import random

x = random.normal(size=(2,3))
print(x)

# генеруємо випадковий нормальний розподіл розміром 2х3 із
# середнім значенням 1 і стандартним відхиленням 2
x = random.normal(loc=1,scale=2,size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(size=1000), hist=False)
plt.show()