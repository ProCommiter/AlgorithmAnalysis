import numpy as np
import random
import math
import time

'''
NOTE: the algorithm works only for n = 2^i

Running time of matrix_multiply = O(n^3)

Running time of recursive_multiply:
    Let T(n) be the running time of recursive_multiply
    T(n) = 8T(n/2) + O(n^2) and T(1) = O(1)
    T(n) = O(n^(log 8)) = O(n^3)

Running time of strassen_multiply:
    Let T(n) be the running time of strassen_multiply
    T(n) = 7T(n/2) + O(n^2) and T(1) = O(1)
    T(n) = O(n^(log 7)) = O(n^2.81)
'''

def split(matrix):
    row, col = matrix.shape
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

#BRUTE FORCE OF MATRIX MULTIPLY
def matrix_multiply(A,B,n):
    C = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

#RECURSIVE MATRIX MULITPLICATION ALGORITHM
def recursive_multiply(A,B):
    if len(A) == 1:
        return A*B

    n = len(A)
    a,b,c,d = split(A)
    e,f,g,h = split(B)

    c11 = recursive_multiply(a,e) + recursive_multiply(b,g)
    c12 = recursive_multiply(a,f) + recursive_multiply(b,h)
    c21 = recursive_multiply(c,e) + recursive_multiply(d,g)
    c22 = recursive_multiply(c,f) + recursive_multiply(d,h)

    C = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return C


#STRASSEN MATRIX MULTIPLICATION ALGORITHM
def strassen_multiply(A,B):
    if len(A) == 1:
        return A*B

    a,b,c,d = split(A)
    e,f,g,h = split(B)

    p1 = strassen_multiply(a, f - h)
    p2 = strassen_multiply(a + b, h)
    p3 = strassen_multiply(c + d, e)
    p4 = strassen_multiply(d, g - e)
    p5 = strassen_multiply(a + d, e + h)
    p6 = strassen_multiply(b - d, g + h)
    p7 = strassen_multiply(a - c, e + f)

    c11 = p5+p4-p2+p6
    c12 = p1+p2
    c21 = p3+p4
    c22 = p1+p5-p3-p7

    C = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return C

def main():
    n = 8
    A = np.zeros((n,n))
    B = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            B[i][j] = random.randint(1,20)
            A[i][j] = random.randint(1,20)

    print("2D matrix for the problem")
    print(A)
    print(B)

    matrix_multiply_start = time.time()
    result = matrix_multiply(A,B,n)
    matrix_multiply_end = time.time()

    print("Result of brute force with time:", matrix_multiply_end-matrix_multiply_start)
    print(result)

    recursive_multiply_start = time.time()
    recursive = recursive_multiply(A,B)
    recursive_multiply_end = time.time()

    print("Result of recursive multiply with time:", recursive_multiply_end-recursive_multiply_start)
    print(recursive)

    strassen_multiply_start = time.time()
    strassen = strassen_multiply(A,B)
    strassen_multiply_end = time.time()

    print("Result of strassen multiply with time:", strassen_multiply_end-strassen_multiply_start)
    print(strassen)


if __name__ == '__main__':
    main()
