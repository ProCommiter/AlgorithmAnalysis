import random
import numpy as np

'''
Loop invariant:
    Let x = arr[r]. At the beginning of each iteration of the for loop in procedure partition(arr,l,r), for any array index k
        1.if l <= k <= i then arr[k] <= x
        2.if i+1 <= k <= j-1 then arr[k] > x
        3.if k = r then arr[k] = x

    Proof:
        We prove the invariant by induction on j. For j = l, i = l-1. No arr[k] with l <= k <= i, no arr[k] with i+1 <= k <= j-1.
        So the invariant holds. Assume the invariant is true for j-1 >= l and we prove it for j.
        There are two cases, (1) arr[j] > x and (2) arr[j] <= x. For (1), the loop only increases j by 1.
        So, arr[j-1] > x and condition 2 holds. The other two conditions are also true.
        For (2), the loop increases i by 1, exchange arr[i] and arr[j], and then increase j by 1.
        By the exchange, arr[i] <= x and Condition 1 holds, and arr[j] > x since the element exchanged to arr[j] is greater than x by the induction hypothesis.
        After j is increased, arr[j-1] > x and Condition 2 holds. Condition 2 is true. So, the invariant is proved.

Running Time:
    The running time of partition(arr,l,r) is O(r-l).
    Worse case partitionl, one subproblem has size n-1 and the other has size 0.
        T(n) = T(n-1) + T(0) + O(n) = T(n-1) + O(n) = O(n^2).
    Best case partition, each subproblem has size n/2
        T(n) = 2T(n/2) + O(n) = O(n log n).
    Average-case running time O(n log n), close to the best-case
        Intuition, for any constant 0 < c < 1, if one subproblem has size cn and the other has size (1-c)n then
        T(n) = T(cn) T((1-c)n) + O(n) = O(n log n)
'''
def partition(arr, l, r):
    x = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quicksort(arr, l, r):
    if l < r:
        q = partition(arr, l, r)
        quicksort(arr, l, q-1)
        quicksort(arr, q+1, r)


def main():
    arr = np.zeros(10)
    for i in range(10):
        arr[i] = random.randint(1,100)

    print("Before Quicksort")
    print(arr)
    print("After Quicksort")
    quicksort(arr, 0, 9)
    print(arr)

if __name__ == '__main__':
    main()
