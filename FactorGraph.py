# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:59:54 2019

@author: Michael
"""
import matplotlib.pyplot as plt

def phi(n):
    nums = []
    divisors = []
    dist = []
    for i in range(2,n):
        nums.append(i)
        divisors.append(0);

    for i in range(len(nums)):
        for div in range(1,(int((nums[i])))):
            if nums[i] % (div) == 0:
                divisors[i] += 1
    for i in divisors:
        if i > len(dist) - 1:
            while i > len(dist) - 1:
                dist.append(0)
        else:
            dist[i] += 1

    print("Graph of the number of divisors")
    plt.plot(nums, divisors,'.')
    plt.show()
    print("Graph of how many numbers in the range have n divisors")
    plt.plot(range(len(dist)),dist, '.')
    plt.show()
    print("Graph of the average number of factors over all ranges in the given range from one to m to one to n")
    histFactors(n)
    
def returnNumFactors(n, Total):
    nums = []
    divisors = []
    for i in range(2,n):
        nums.append(i)
        divisors.append(0);

    for i in range(len(nums)):
        for div in range(1,(int((nums[i])))):
            if nums[i] % (div) == 0:
                divisors[i] += 1
    if (Total):
        return sum(divisors)
    else:
        return float(sum(divisors) / n)

def histFactors(n):
    hist = []
    for i in range(1,n):
        if returnNumFactors(i, False) > len(hist):
            while returnNumFactors(i, False) > len(hist):
                hist.append(0)
        else:
            hist.append(returnNumFactors(i, False))
    plt.plot(range(len(hist)), hist)
    
    file = open("data.txt","a")
    for i in range(len(hist)):
        file.write(str(hist[i]) + ",\n")
    file.close()
