# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:05:44 2018

@author: sagarikatalla

HACKERRANK
"""
'''###### longest common subsequence ####'''
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
def LCS(X,Y):
    m=len(X)
    n =len(Y)
    
    L = [[None]*(n+1) for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if  i==0 or j==0:
                L[i][j]=0
            elif X[i-1]==Y[j-1]:
                L[i][j]=1+L[i-1][j-1]
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
                
    return L[m][n]                
                
LCS(X = 'AGGTAB',Y ='GXTXAYB')

'''### sam and substrings(continuous string) sum ##'''
## formula si = si. sigma(10**i(i+1))
def substrings(n):
    l = len(n)
    w =[1]*l
    ws = [1]*l
    for i in range(1,l):
        w[i] = w[i-1]*10
        ws[i]=ws[i-1]+w[i]

    res =0
    for i in range(l):
        v = int(n[i])* ws[l-i-1]*(i+1)
        print(n[i], ws[l-i-1],v)
        res = res + v
    
    return(res)

substrings('1234')
substrings('23')

##Longest common subsequence

##Knapsack problem

## reduced substring delete adjacent same letters

def sub(s):
    ls =[]
    for c in st:
        if ls and ls[len(ls)-1]==c:
            ls.pop()
        else:
            ls.append(c)
    return ls or 'Empty String'

st = 'aabccb'
sub(st)


###
#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true
def isValid(s):
    #count number of times each letter appears .count() = ls
    #check if count is same for all,return 'Yes'  
    #else count unequal: 
    # aabbccd     
    # aaabbbcccc equal  and uneq
    # No : abcdd
    dict = {}
    for i in s:
        dict[i] =s.count(i)

    count ={}
    for key,val in sorted(dict.items()):
        count[val] = count.get(val,0)+1

    print(count,dict)
    x = []
    y = []
    if len(count)==2:
        for i,j in sorted(count.items()):
            x.append(i)
            y.append(j)
        print(x,y)


    if len(count)>2:
        
        return 'NO'
    else:    
        if  len(count)==1:
            return 'YES'
        elif len(count)==2:
            if (x[1]-x[0]==1 and y[1] ==1) or (x[0]==1 and y[0]==1) :
                return 'YES'
            
            else:
                return 'NO'
        else:
            return 'NO'
    #aaaabbcc
    #aabbc

isValid('aabbc')

##alternate way
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    # frequencies of all letters
    freq = Counter(s)
    # frequencies values sorted
    values = sorted(freq.values())
    # max frequencie value
    v_max = max(values)
    # min frequencie value
    v_min = min(values)
    # max frequencie value repetitions
    max_count = values.count(v_max)
    # min frequencie value repetitions
    min_count = values.count(v_min)
    # frequencie of frequencie values, made some validations more easy 
    freq_values = Counter(values)

    # more then 2 frequencies repeat, this case string can be valid, case: aaabbc
    if len(freq_values) > 2:
        return 'NO'
    # only 1 frequencie repeat, so, is a valid string, case: aabbcc
    elif len(freq_values) == 1:
        return 'YES'
    # min frequencie count is 1, so, just remove one value to turn the string valid, case: aab
    elif min_count == 1:
        return 'YES'
    # max frequencie minus your repeatitions equal min value, case: bbaaa, just remove
    # one of the same letter repetitions to turn the strig valid
    elif v_max - max_count == v_min:
        return 'YES'
    # other cases are not valids
    else:
        return 'NO'