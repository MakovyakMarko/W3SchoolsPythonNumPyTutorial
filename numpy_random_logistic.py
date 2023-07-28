# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:30:36 2023

@author: Marko
"""

from numpy import random
x = random.logistic(loc=1,scale=2,size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()

# різниця між логістичним і нормальним роподілом
sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
plt.show()