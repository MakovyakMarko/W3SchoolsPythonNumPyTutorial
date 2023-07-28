# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:19:56 2023

@author: Marko
"""

from numpy import random

x = random.chisquare(df=2, size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=1, size=1000),hist=False)
plt.show()