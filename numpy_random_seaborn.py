# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 11:43:40 2023

@author: Marko
"""

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0,1,2,3,4,5])
plt.show()

sns.distplot([0,1,2,3,4,5], hist=False)
plt.show()