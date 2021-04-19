import numpy as np
import random
import randomized_quicksort

'''
Selection problem: Given a set of arr of n numbers and an integer i with 1<=i<=n, find the element x in arr that is larger than exactly i-1 other elements of arr.

Running time:
    It takes O(n) comparisons to find the Minimum
    It takes O(n) comparisons to find the Maximum

    A brute-force approach: sort n elements and get the ith one in the sorted list, O(n log n) time.

    The average running time of randomized_select is O(n)
'''

def randomized_select(arr,l,r,i):
    if l == r:
        return arr[l]

    q = randomized_quicksort.randomized_partition(arr,l,r)
    k = q-l+1

    if i == k:
        return arr[q]
    elif i < k:
        return randomized_select(arr,l,q-1,i)
    else:
        return randomized_select(arr,q+1,r,i-k)

def minimum(arr):
    min_num = arr[0]
    for i in range(1, len(arr)):
        if min_num > arr[i]:
            min_num = arr[i]
    return min_num

def maximum(arr):
    max_num = arr[0]
    for i in range(1, len(arr)):
        if max_num < arr[i]:
            max_num = arr[i]
    return max_num

def main():
    arr = np.zeros(10)
    for i in range(10):
        arr[i] = random.randint(1,100)
    print("Array")
    print(arr)
    min_num = minimum(arr)
    max_num = maximum(arr)
    print("Minimum from array is", min_num)
    print("Maximum from array is", max_num)
    print("4th smallest number in array is",randomized_select(arr,0,9,4))
    print("Sorted array")
    randomized_quicksort.randomized_quicksort(arr,0,9)
    print(arr)

if __name__ == '__main__':
    main()
