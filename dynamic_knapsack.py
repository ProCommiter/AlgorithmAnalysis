import numpy as np
import random

'''
Structure:
    Let opt(i,w) = max-value of items 1,...,i with weight limit w. The goal is to find opt(n,W)
    Case 1: opt(i,w) does not select item i but the best of {1,...,i-1} using weight limit w.
    Case 2: opt(i,w) selects item i and the best of {1,...,i-1} using weight limit w-wi

Bellman Equation:
    opt(i,w) =  0                                   , if i = 0
                opt(i-1, w)                         , if wi > w
                max(opt(i-1,w), vi + opt(i-1, w-wi)), otherwise

Running Time:
    Knapsack algorithm finds opt(n,W) in O(nW) time and O(nW) space. This is not a poly(n) time algorithm when W is not upper bounded by poly(n)
    We can be as large as 2^(cn) for c > 0
'''

def knapsack(W, wt, val, n):
    M = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                M[i][w] = 0
            elif wt[i-1] <= w:
                M[i][w] = max(val[i-1] + M[i-1][w-wt[i-1]], M[i-1][w])
            else:
                M[i][w] = M[i-1][w]

    return M[n][W]

def main():
    val = [1,6,18,22,28]
    wt = [1,2,5,6,7]
    W = 11
    n = len(val)

    print("Dynamic Programming for 0-1 Knapsack")
    print("Values and Weights")
    print(val)
    print(wt)

    print("Knapsack can only hold the weight of", W, "amount", end = " ")
    print(knapsack(W,wt,val,n), "is the maximum profit")

if __name__ == '__main__':
    main()
