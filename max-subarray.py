import numpy as np
import random
import math

'''
Correctness of Find Maximum-Subarray

    Loop invariant: At start of each iteration of loop 'for i = m downto l do', get left_sum, and sum holds the sum of elements in arr[i..m].

    Initialization: For i = m, no sum is computed and the invariant is true.

    Maintenance: Assume that the invariant holds for i + 1 <= m. In the ith iteration, sum = sum + arr[i], so sum holds the sum of elements of arr[i+1..m] and arr[i].
    and if sum > left_sum then left_sum is updated to sum.

    Termination: When the loop terminates, left_sum = max(left_sum, right_sum, left_sum+right_sum)
    Since max_subarray(arr,l,m) finds the largest subarray in arr[l..m],
    max_subarray(arr, m+1, r) finds the largest subarray in arr[m+1...r] and
    max_crossing(arr,l,m,r) finds the largest subarray arr[x..y] for any l <= x <= m and any m+1 <= y <= r, the algorithm is correct

Running Time:
    Let T(n) be the running time of max_subarray
    Let t(n) be the running time of max_crossing
    then T(n) = 2T(n/2) + t(n) + O(1) and T(1) = O(1)
    From t(n) = O(n), T(n) = O(n log n)
'''
def max_crossing(arr, l, m, r):

    sum = 0
    left_sum = -math.inf
    for i in range(m, l-1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            c_i = i

    sum = 0
    right_sum = -math.inf
    for j in range(m+1, r+1):
        sum += arr[j]
        if sum > right_sum:
            right_sum = sum
            c_j = j

    return c_i, c_j, left_sum+right_sum


def max_subarray(arr, l, r):
    #base case 1 element
    if (l == r):
        return l,r,arr[l]

    m = (l+r)//2

    l_i, l_j, L = max_subarray(arr, l, m)
    r_i, r_j, R = max_subarray(arr, m+1, r)
    c_i, c_j, C = max_crossing(arr, l, m, r)

    if L >=R  and L >= C:
        return l_i, l_j, L
    elif R >= L and R >= C:
        return r_i, r_j, R
    else:
        return c_i, c_j, C

def main():
    n = 10
    arr = [0] * n
    for i in range(n):
        arr[i] = random.randint(-100,100)

    print("Array for the problem")
    print(arr)

    i,j,result = max_subarray(arr,0,n-1)

    print("the maximum subarray is sum of", result, "from", i, "to", j)

if __name__ == '__main__':
    main()
