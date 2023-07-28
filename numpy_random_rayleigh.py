# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:22:49 2023

@author: Marko
"""

from numpy import random

x = random.rayleigh(scale=2,size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()