import numpy as np
import random
import math
import Insertion_Sort

'''
Running Time:

    bucket_sort sorts a1,...,an in [0,1) in worst case time O(n^2) and in average time O(n)
    When a1,...,an are uniformly and independently distributed in [0,1).

    Proof. For ai <= aj, since floor(n*ai) <= floor(n*aj), either ai and aj are put in a same bucket or ai is put a bucket with a smaller index.
    If ai and aj are in the same bucket, then they are put in the correct order by the insertion sort.
    Otherwise, they are put in the correct order by the concatenation of the bucket lists.

    Let ni be the number of elements in bucket B[i]. Then sum of (i=1 to n-1) ni = n.
    Let T(n) be the running time bucket_sort. Then T(n) = O(n)+ sum of(i=1 to n-1) O(ni^2) = O(n^2).
    So, in worst case, T(n) = O(n^2).
    It can be shown that E[ni^2] = 2-1/n for every i when a1,...,an are uniformly and independently distributed in [0,1).
    So, the average running time is O(n).
'''
def bucket_sort(arr):
    n = len(arr)
    B = []

    for i in range(n):
        B.append([])

    for j in arr:
        index_b = int(n*j)
        B[index_b].append(j)

    for i in range(n):
        B[i] = Insertion_Sort.insertion(B[i])

    k = 0
    for i in range(n):
        for j in range(len(B[i])):
            arr[k] = B[i][j]
            k += 1

    return arr

def main():
    arr = np.zeros(10)
    for i in range(10):
        arr[i] = random.uniform(0,1)
    print("Before Bucket Sort")
    print(arr)
    print("After Bucket Sort")
    res = bucket_sort(arr)
    print(res)

if __name__ == '__main__':
    main()
