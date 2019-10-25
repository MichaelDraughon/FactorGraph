# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:59:54 2019

@author: Michael
"""
import matplotlib.pyplot as plt

def main():
    nums = []
    divisors = []
    for i in range(2,10000):
        nums.append(i);
        divisors.append(0);
    
    for i in range(len(nums)):
        for div in range(1,(int((nums[i] ** (0.5))) + 1)):
            if nums[i] % (div) == 0:
                divisors[i] += 1
    
    plt.plot(nums, divisors, 'o');
    plt.show();