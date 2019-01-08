# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:40:40 2019

@author: Manika

Statistics Challenge:  Calculate mean, median and mode for the input
                       Print the lowest value if there are multiple modes
"""
import numpy as np
import statistics as stat

n = int(input("Enter number of integers in array: "))
numbers = input("Enter the integers in array separated by a space: ")
num = list(numbers.split())

values = [int(value) for value in num]
print(values)

#Calculate mean
mean = np.mean(values)
print("Mean: %.1f" % mean)

#Calculate median
median = stat.median(values)
print("Median: %.1f" % median)

#Calculate mode
def mode(array):
    cnt = max(list(map(array.count, array)))
    return list(set(filter(lambda x: array.count(x) == cnt, array)))

modes = mode(values)
min_mode = min(mod for mod in modes)
print("Mode:", min_mode)