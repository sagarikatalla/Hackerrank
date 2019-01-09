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
    print(arr)
    return arr[m][n]


LCS("AGGTAB","GXTXAYB")
#Time complexity
#O(mn)

# A Naive recursive Python implementation of LCS problem 
  
def lcs(X, Y, m, n): 
  
    if m == 0 or n == 0: 
       return 0; 
    elif X[m-1] == Y[n-1]: 
       return 1 + lcs(X, Y, m-1, n-1); 
    else: 
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 
  
  
# Driver program to test the above function 
X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is ", lcs(X , Y, len(X), len(Y)) 

###Time complexity = O(2^n)
#T(1) = O(1)
#and
#T(N) = O(1) + 2*T(N-1) when N>1
#If you repeatedly expand the last term, you get:
#
#T(N) = 3*O(1) + 4*T(N-2)
#T(N) = 7*O(1) + 8*T(N-3)
#...
#T(N) = (2^(N-1)-1)*O(1) + (2^(N-1))*T(1)
#T(N) = (2^N - 1)*O(1)
#T(N) = O(2^N)
