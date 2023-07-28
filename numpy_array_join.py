# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 12:16:45 2023

@author: Marko
"""

import numpy as np

# Об'єднання масивів 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1,arr2))
print(arr)
# З'єднайте 2 2д масиви вздовж рядків (вісь=1)
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
arr3 = np.concatenate((arr1,arr2), axis=1)
print(arr3)
# Об'єднання масивів за допомогою стекових функцій
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.stack((arr1,arr2), axis=1)
print(arr)
# Укладання вздовж рядків
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.hstack((arr1,arr2))
print(arr)
# Укладання вздовж стовпців
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.vstack((arr1,arr2))
print(arr)
# Укладання по висоті (глибина)
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.dstack((arr1,arr2))
print(arr)