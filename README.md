# Algorithm Analysis

The Python code references the pseudocode from Cormen, T. H., & Leiserson, C. E. (2009). Introduction to algorithms, 3rd edition.
https://sd.blackball.lv/library/Introduction_to_Algorithms_Third_Edition_(2009).pdf

The repository is made for better understanding of algorithm analysis (e.g. Binary Heap).

    A one-dimensional array A viewed as a nearly complete binary tree T.
    Each element of A corresponds to a node of T:
        A[1] is the root of T.
        For i >= 1, A[2i] is the left child of A[i], A[2i+1] is the right child of A[i].
        For i >= 2, A[floor(2i)] is the parent of A[i].

    Basic functions:
        Parent(i)
            return floor(i/2)
        Left(i)
            return 2i
        Right(i)
            return 2i+1
        Max-Heap
            A[floor(i/2)] >= A[i]
        Min-Heap
            A[floor(i/2)] <= A[i]

    Basic operations on max-heaps:
        Max-heapify
            maintain the max-heap property in O(log n) time.
        Build-max-heap
            build a max-heap from an unordered array in O(n) time.
        Heapsort
            sort an array in ascending order in O(n log n) time.
        Max-heap-increase-key
            increase the value of one element and then maintain the max-heap property in O(log n) time.
        Max-heap-insert
            insert a new element to a max-heap and then maintain the max-heap property in O(log n) time.
        Heap-Maximum
            return the maximum element of a max-heap
        Max-Heap-Delete
            delete the maximum element from a max-heap and then maintain the max-heap property in O(log n) time.
