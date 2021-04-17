import random
import numpy as np

'''
Loop invaraint: At the start of each iteration of the loop 'for k = l to r do' in the subroutine Merge, the subarray arr[l..k-1] contains the k-l smallest
elements of L[1.. n_l + 1] and R[1... n_r + 1] in sorted order. Further, L[i] and R[j] are the smallest elements of these in L and R not copied to A.

    Initialization: For k = l, arr[l...k-1] is empty and i = j = 1. Hence, arr[l..k-1] has 0 smallest elements of L and R, both L[i] and R[j] are the smallest
    of these in L and R

    Maintenance: Assume the invariant is true for k-1 >= l and we prove it for k. Assume L[i] <= R[j]. Then L[i] is the smallest element not copied to A yet.
    Because A[l...k-1] has the k-l smallest elements, after L[i] is copied to A[k], A[l..k] has k-l+1 smallest elements.
    Incrementing k and i reestablishes the invariant for the next iteration. The proof for case L[i] > R[j] is similar.

    Termination: At termination of Merge, k = r+1. By the invariant above, arr[l..k-1] = arr[l..r] has r-l+1 smallest elements of L[1..n_l+1] and R[1..n_r+1] in sorted order.
    L and R have n_l + n_r + 2 = r - l + 3 elements. All  but two elements of infinity have been copied back to arr. So, when mergesort terminates, A has n elements in sorted order.

Running Time:

    Let T(n) be the running time of mergesort. T(1) = c, c > 0 a constant.
    Divide array of size n takes cn time
    Recursion on array of size n/2 takes T(n/2) time.
    Merge two arrays of size n/2 take cn Time
    T(n) = cn + T(n/2) + T(n/2) + cn
         = O(n logn)
'''
def sort(arr):

    if len(arr) > 1:

        mid = len(arr)//2
        L = arr[:mid].copy()
        R = arr[mid:].copy()

        sort(L)
        sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def main():
    arr = np.zeros(10)
    for i in range(10):
        arr[i] = random.randint(1,100)

    print("Before Insertion-sort")
    print(arr)

    sort(arr)

    print("After Insertion-sort")
    print(arr)

if __name__ == '__main__':
    main()
