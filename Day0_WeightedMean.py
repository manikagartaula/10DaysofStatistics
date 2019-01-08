# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:40:57 2019

@author: Manika
Statistics Challenge: Calculate weighted mean of an array
"""
n = int(input())
numbers = input()
weights = input()

number = list(numbers.split())
num = [int(n) for n in number]

weight = list(weights.split())
wt = [int(w) for w in weight]

#Calculate weighted mean
def weighted_mean(array, wgt, n):
    meansum = 0
    weightsum = 0
    for i in range(0, n):
        meansum = meansum + (array[i]*wgt[i])
        weightsum = weightsum + wgt[i]
    return meansum/weightsum

wt_mean = weighted_mean(num, wt, n)
print("%.1f" % wt_mean)
