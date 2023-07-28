# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 11:56:13 2023

@author: Marko
"""
from numpy import random
# з огляду на 10 випробувань підкидання монети генеруємо 10 точок даних:
x = random.binomial(n=10, p=0.5, size=10)
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()

# різниця між нормальним і біноміальним роподілом
sns.distplot(random.normal(loc=50, scale=5, size=1000),hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()