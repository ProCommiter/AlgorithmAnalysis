import numpy as np
import random

'''
Running Time:

    Given n d-digit numbers, each digit can take most k different values, radix_sort sorts the numbers in O(d(n+k)) time if the stable sort used takes
    O(n+k) time.

    Proof. We show by induction on i the invariant that the numbers are sorted on the least significant i digits.
    The invariant is true for i = 1. Assume the invariant holds for i-1 >= 1 and we prove it for i.
    The numbers are sorted on digit i. For the numbers with the same value on digit i, because a stable sort is used,
    they are sorted on the least significant i-1 digits. Therefore, the invariant holds, implying radix sort sorts the numbers.
    It takes O(n+k) time to sort on one digit, giving a total O(d(n+k)) time. 
'''
def counting_sort(arr,k, d):
    n = len(arr)
    output = [0] * 10
    count = [0] * k

    for i in range(0, n):
        index = arr[i] // d
        count[index % 10] += 1

    for i in range(1,k):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        index = arr[i] // d
        output[count[index%10]-1] = arr[i]
        count[index%10] -= 1
        i -= 1

    for i in range(0, n):
        arr[i] = output[i]

def radix_sort(arr, k):
    max_num = max(arr)

    d = 1
    while max_num // d > 0:
        counting_sort(arr,k, d)
        d *= 10

def main():
    arr = [0]*10
    k = 20
    for i in range(10):
        arr[i] = random.randint(1,k)

    print("Before Radix Sort")
    print(arr)
    print("After Radix Sort")
    radix_sort(arr, k+1)
    print(arr)

if __name__ == '__main__':
    main()
