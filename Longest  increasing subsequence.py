# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 22:44:30 2019

@author: sagarikatalla
"""

def LIS(s): 
    l = [1]*len(s)
    for i in range(1,len(s)):
        for j in range(0,i):
            if s[i]>s[j] and l[i]<l[j]+1:
                l[i] = l[j]+1
                print(l,l[i],l[j])
    
    return max(l)

LIS(s = [10, 22, 9, 33, 21, 50, 41, 60])
    
    
    
    
    
    
 
    
    
arr = [10, 22, 9, 33, 21, 50, 41, 60] 
print "Length of lis is", lis(arr) 