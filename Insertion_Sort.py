import random
import numpy as np

'''
Correctness of Insertion-Sort:
    Loop invariant for Insertion-Sort: at start of each iteration of the for loop, subarray A[1..j-1] holds the elemnts originally in A[1..j-1] and sorted

    Initialization: For j = 2, arr[1..j-1] = arr[1] has one element and the invariant is true

    Maintenance: Assume the invariant holds for j-1 >= 2 and we prove the invariant for j. In the for loop, the element originally in arr[j] is assigned to tmp
    each element arr[i] with tmp < arr[i] is moved to arr[i+1] for i = j-1, j-2, ..., and tmp is assigned to arr[i] s.t. arr[i-1] <= tmp.
    From this and induction hypothesis, arr[1...j] holds the elements originally in arr[1...j].
    Further, arr[1..i-1] is sorted, arr[i+1,..j] is sorted and arr[i-1] <= tmp < arr[i+1], arr[1...j] is sorted.
    Thus sthe invariant holds for j.

    Termination: Algorithm teminates after the iteration for j = n. By the invariant above, the algorithm outputs the array arr[1..n] in sorted order

Running Time:
    Best Case = O(1) ex) when everything is sorted
    Worst Case = O(n^2) ex) arr[1] > arr[j]
    Average Case = O(n^2) ex) arr[j/2] <= arr[j] and arr[j/2+1] > arr[j]
'''

def insertion(arr):

    for j in range(2,len(arr)):

        tmp = arr[j]
        i = j-1

        while i >= 0 and arr[i] > tmp:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = tmp
        
    return arr


def main():
    #array will consist of n elements
    n = 10

    arr = np.zeros(n)
    #make array with random elements
    for i in range(n):
        arr[i] = random.randint(1,100)

    print("Before Insertion-sort")
    print(arr)

    arr = insertion(arr)
    print("After Insertion-sort")
    print(arr)

if __name__ == '__main__':
    main()
