# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:59:54 2019

@author: Michael
"""
import matplotlib.pyplot as plt

def main(n):
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

    plt.plot(nums, divisors,'.')
    plt.show()
    plt.plot(range(len(dist)),dist, )
    plt.show()
    #print(divisors[len(divisors) - 1])

    #for i in range(len(divisors) - 1):
    #    print(divisors[i])
