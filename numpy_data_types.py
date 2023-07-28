# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:29:12 2023

@author: Marko
"""

# i - ціле число
# b - логічний
# u - ціле число без знаку
# f - числа з плаваючою точкою
# c - комплексні числа з плаваючою точкою
# m - дельта часу
# M - дата, час
# O - об'єкт
# S - строка
# U - строка Unicode 
# V - фіксована частина пам'яті для іншого типу (void)

import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype)

arr = np.array(['apple','banana','chery'])
print(arr.dtype)

# створення масивів із визначеним типом даних
arr = np.array([1,2,3,4], dtype="S")
print(arr)
print(arr.dtype)

# для i,u,f,S,U ми також можемо визначити розмір
arr = np.array([1,2,3,4], dtype='i4')
print(arr)
print(arr.dtype)

# Що робити, якщо значення не можна перетворити?
#arr = np.array(['a','2','3'], dtype='i')

# Функція astype() створює копію масиву та дозволяє 
# вказати тип даних як параметр
arr = np.array([1.1,2.1,3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

arr = np.array([1,0,3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
