# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:25:35 2023

@author: Marko
"""

from numpy import random

x = random.pareto(a=2, size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()