# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:11:41 2023

@author: Marko
"""

import numpy as np
# розрізання в Python означає перенесення елементів з 
# одного даного індексу в інший заданий індекс
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])
# пеший індекс включно, але другий індекс виключно
print(arr[4:])
print(arr[:4])
# негативний слайсінг
print(arr[-3:-1])
# крок - це третій індекс
print(arr[1:5:2])
print(arr[::2])

# слайсінг 2-D масивів
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# з другого масиву елементи від індексу 1 до 4 (не включено)
print(arr[1,1: 4])
# з обох масивів повернути індекс 2
print(arr[0:2, 2])
# з обох масивів від індексу 1 до індексу 4(не включено)
# поверне 2-D масив
print(arr[0:2, 1:4])