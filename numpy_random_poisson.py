# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:16:48 2023

@author: Marko
"""

from numpy import random
x=random.poisson(lam=2, size=10)
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()
# різниця між нормальним роподілом і розподілом Пуассона 
sns.distplot(random.normal(loc=50,scale=7,size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show()
# різниця між біноміальним роподілом і розподілом Пуассона
sns.distplot(random.binomial(n=1000, p=0.01,size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
plt.show()