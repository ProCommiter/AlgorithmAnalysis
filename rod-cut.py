import numpy as np
import random
import math
import time

'''
Rod cutting problem:
    Given a rod R of length n inches and a table of prices pi for i = 1,2,..,n, find the max revenue rn obtainable by cutting R and selling the pieces.
    there are at most 2^(n-1) ways to cut R as each of 1 <= i <= n-1 inch positions from one end of R,we can cut or not

Running time of cut_rod(p,n):
    Let T(n) be the running time of cut_rod.
    T(n) = 1 + sum of (j = 0 to n-1) T(j) = O(2^n), not efficient because a same subproblem may be solved repeatedly

Dynamic programming approach for rod-cutting:
    Memoization: solve a subproblem only once and keep the solution in a table for later reference to save time (time-memory trade-off).
    Tow approaches: top-down with memoization and bottom-up method.

Both memoized-cut-rod and bottom-up-cut-rod take O(n^2) time.
'''
#A top-down recursive algorithm for rod-cutting
def cut_rod(p,n):
    if n == 0:
        return 0
    q = -math.inf
    for i in range(1, n+1):
        q = max(q, p[i]+cut_rod(p, n-i))
    return q

#Dynamic programming approach for rod cutting (top-down)
def memoized_cut_rod(p,n):
    r = [0] * n
    for i in range(n):
        r[i] = -math.inf
    return memoized_cut_rod_aux(p,n-1,r)

def memoized_cut_rod_aux(p,n,r):
    if r[n] >= 0:
        return r[n]

    if n == 0:
        return 0
    else:
        q = -math.inf
    for i in range(1,n+1):
        q = max(q,p[i]+memoized_cut_rod_aux(p,n-i,r))
    r[n] = q
    return q

#Dynamic programming approach for rod cutting (bottom up)
def bottom_up_cut_rod(p,n):
    r = [0] * (n+1)
    r[0] = 0
    for j in range(1,n+1):
        q = -math.inf
        for i in range(1,j+1):
            q = max(q, p[i] + r[j-i])
        r[j] = q
    return q

def extended_bottom_up_cut_rod(p,n):
    r = [0] *(n+1)
    s = [0] *(n+1)
    for j in range(1,n+1):
        q = -math.inf
        for i in range(1, j+1):
            if q < p[i]+r[j-i]:
                q = p[i]+r[j-i]
                s[j] = i
        r[j] = q
    return r, s

def print_cut_rod_solution(p,n):
    r, s = extended_bottom_up_cut_rod(p,n)
    while n > 0:
        print(s[n], end = " ")
        n = n-s[n]

def main():
    p = [0,1,5,8,9,10,17,17,20,24,30]
    n = 7

    print("Price array")
    print(p)

    print("\nRod cutting problem using recursive algorithm")
    recurse_start = time.time()
    print(cut_rod(p,n))
    recurse_end = time.time()
    print("It takes", recurse_end-recurse_start, "for using recursive algorithm \n")

    print("Rod cutting problem using Dynamic Programming TOP DOWN approach")
    top_start = time.time()
    print(memoized_cut_rod(p,n+1))
    top_end = time.time()
    print("It takes", top_end-top_start, "for using top down approach\n")

    print("Rod cutting problem using Dynamic Programming BOTTOM UP approach")
    top_start = time.time()
    print(bottom_up_cut_rod(p,n))
    top_end = time.time()
    print("It takes", top_end-top_start, "for using top down approach")

    print("\nThe solutions for cut rod problem is cutting with", end = " ")
    print_cut_rod_solution(p,n)
    print("")

if __name__ == '__main__':
    main()
