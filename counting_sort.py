import numpy as np
import random

'''
Running Time:
    Counting sort sorts n integeters in range [0,k] in O(k+n) time.

    Proof. At the end of the 2nd for loop, each C[i] holds the number of elements equal to i for each i = 0, 1, ..., k.
    At the end of the 3rd for loop, each C[i] holds the number of elements at most i.
    At the end of the 4th for loop, for each A[j], C[A[j]] is the correct final position of A[j] in array B ecause there are C[A[j]] elements at most A[j].
    Decrementing C[A[j]] causes the next input element = A[j] placed at the position immediately before A[j].

    The running time is O(k+n)

A sorting algorithm is stable if the numbers of the same value appear in the output in the same order as they do in the input, that is,
to sort a1,...,an in ascending order, if ai <= aj with i < j and after sorting ai -> ai' and aj->aj', then i' < j'. Counting sort is stable.
'''
def counting_sort(arr, k):
    n = len(arr)
    B = [0] * n
    C = [0] * k

    for i in range(0, n):
        C[arr[i]] += 1

    for i in range(1, k):
        C[i] += C[i-1]

    i = n - 1
    while i >= 0:
        B[C[arr[i]] - 1] = arr[i]
        C[arr[i]] -= 1
        i -= 1

    for i in range(0, n):
        arr[i] = B[i]

def main():
    arr = [0] * 10
    n = 20
    for i in range(10):
        arr[i] = random.randint(1,n)

    print("Before Counting Sort")
    print(arr)
    print("After Counting Sort")
    counting_sort(arr, n+1)
    print(arr)

if __name__ == '__main__':
    main()
