# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 20:50:44 2019

@author: sagarikatalla
"""
#length of longest subsequennce
#Dynamic programming
def LCS(a,b):
    m = len(a)
    n = len(b)
    arr = [[0]*(n+1) for i in range(m+1)]
    
    #Bottom-up approach
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                arr[i][j]= 0
            #if last letters are same
            elif a[i-1]==b[j-1]:
                arr[i][j]= 1 + arr[i-1][j-1]
            ##if last letters are different
            else:
                arr[i][j]= max(arr[i-1][j],arr[i][j-1])
            
    return arr[m][n]

LCS("AGGTAB","GXTXAYB")