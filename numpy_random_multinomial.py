# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:35:46 2023

@author: Marko
"""

from numpy import random

x = random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(x)