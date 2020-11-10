import timeit
import random
import matplotlib.pyplot as plt
import numpy as np
import time
import math
import copy


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def timSort(arr,k,epochs):
    suma_i = 0
    suma_m = 0
    summma_i = []
    summma_m = []
    ttm = 0
    ttmm = []
    if k >= len(arr[-1]):
        for i in range(len(arr[-1])):
            for j in range(i * epochs, (i + 1) * epochs):
                t1 = time.time()
                insertionSort(arr[j])
                t2 = time.time()
                t = t2 - t1
                ttm = ttm + t
            ttmm.append(100 * ttm / epochs)
        tt = sum(ttmm)
    else:
        for i in range(0,k):
            for j in range(i * epochs, (i + 1) * epochs):
                i_t1 = time.time()
                insertionSort(arr[j])
                i_t2 = time.time()
                inserttime = i_t2 - i_t1
                suma_i = suma_i + inserttime
            summma_i.append(100 * suma_i / epochs)

        for m in range(k, len(arr[-1])):
            for n in range(m  * epochs, (m + 1) * epochs):
                m_t1 = time.time()
                mergeSort(arr[n],0,len(arr[n]) - 1)
                m_t2 = time.time()
                mergetime = m_t2 - m_t1
                suma_m = suma_m + mergetime
            summma_m.append(100 * suma_m / epochs)


        tt = sum(summma_i) + sum(summma_m)
    return tt

def mergeSortt(arr,epochs):
    ttm = 0
    ttmm = []
    for i in range(len(arr[-1])):
        for j in range(i * epochs, (i + 1) * epochs):
            t1 = time.time()
            mergeSort(arr[j], 0, len(arr[j]) - 1)
            t2 = time.time()
            t = t2 - t1
            ttm = ttm + t
        ttmm.append(100 * ttm / epochs)
    tt = sum(ttmm)
    return tt

############# produce random array
def Randomgen(num):
    arr = []
    for i in range(0,num):
        ar = random.randint(0,10)
        arr.append(ar)
    return arr


epochs  = 10

t_1 = []
t_2 = []
num_min = 1
num_max = 100
for num in range(num_min,num_max):
    arr = []
    for i in range(0, num):
        for j in range(epochs):
            ar = Randomgen(i + 1)
            arr.append(ar)


    tt_1 = timSort(arr,2,epochs)
    t_1.append(tt_1)
    tt_2 = mergeSortt(arr,epochs)
    t_2.append(tt_2)


plt.plot(range(num_min, num_max), t_1, c='r', label='timsort')
plt.plot(range(num_min, num_max), t_2, c='b', label='mergesort')
plt.legend()
plt.xlabel("Input size (N)")
plt.ylabel("Scaled Running Time of Algorithm (seconds)")
plt.show()



#References:
# mergesort: https://www.geeksforgeeks.org/python-program-for-merge-sort/
# insertion sort:https://www.runoob.com/python3/python-insertion-sort.html

