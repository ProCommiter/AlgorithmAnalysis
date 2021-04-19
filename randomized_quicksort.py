import random
import numpy as np

'''
Running Time:
    Average running time of randomized-quicksort
        Let x be the number of comparisons performed in randomized-partition over entire execution of randomized-quicksort on an element array.
        then the running time of randomized-quicksort is O(n+X)
        Rename the elements of A as z1,...,zn s.t. z1 <= ... <= zn.
        Any zi and zj are compared at most once over entire execution of randomized-quicksort because each element is compared only to a pivot
        and an element is selected as a pivot at most once (zi and zj are compared iff xi or xj is selected as a pivot and the pivot is not involved
        in the recursive sortings).
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

def randomized_partition(arr,l,r):
    i = random.randint(l,r)
    arr[i], arr[r] = arr[r], arr[i]
    return partition(arr,l,r)

def randomized_quicksort(arr,l,r):
    if l < r:
        q = randomized_partition(arr,l,r)
        randomized_quicksort(arr,l,q-1)
        randomized_quicksort(arr,q+1,r)

def main():
    arr = np.zeros(10)
    for i in range(10):
        arr[i] = random.randint(1,100)

    print("Before Quicksort")
    print(arr)
    print("After Quicksort")
    randomized_quicksort(arr, 0, 9)
    print(arr)

if __name__ == '__main__':
    main()
