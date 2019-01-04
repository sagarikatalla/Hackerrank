# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 13:42:53 2019

@author: sagarikatalla
"""
## recursion approach
def fib(n):
    if n ==1 or n==2:
        return 1 #base case
    else:
        return fib(n-1)+fib(n-2)
    
fib(12)
    
## dynamic programming
##give up space for time allocating arrays
def fibmem(n):
    
    x=[0,1]
    while len(x)<n+1:
        x.append(0)
    
    if n<=1:
        return n
    else:
        if x[n-1]==0:
            x[n-1]= fibmem(n-1)
        if x[n-2]==0:
            x[n-2]= fibmem(n-2)
        x[n] = x[n-1]+x[n-2]
    return x[n]

fibmem(4)
    

fibmem(n=5)
