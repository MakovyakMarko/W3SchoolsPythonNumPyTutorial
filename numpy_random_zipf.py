# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:29:36 2023

@author: Marko
"""

from numpy import random

x = random.zipf(a=2, size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()