# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:26:29 2023

@author: Marko
"""

from numpy import random
x = random.uniform(size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=1000), hist=False)
plt.show()