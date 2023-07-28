# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:15:06 2023

@author: Marko
"""

from numpy import random

x = random.exponential(scale=2, size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(size=1000), hist=False)
plt.show()

# роподіл Пуассона стосується кількості подій за певний період
# часу, тоді як експоненціальний роподіл має справу з часом
# між цими подіями