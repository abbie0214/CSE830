import timeit
import random
import matplotlib.pyplot as plt
import numpy as np
import time
import math
import copy


def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1
        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1
        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def timSort(arr,k):
    if len(arr) > 1:
        if k > len(arr):
            insertionSort(arr)
        else:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            timSort(L, k)
            timSort(R, k)
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
    return arr



def test(num, epochs):
    summma_m = []
    summma_i = []
    summma_t = []
    for i in range(0,num):
        suma_m = 0
        suma_i = 0
        suma_t = 0
        for j in range(0, epochs):
            arr = list(np.random.randint(i,size = i))
            arr_2 = copy.deepcopy(arr)
            arr_3 = copy.deepcopy(arr)

            m_t1 = time.time()
            mergeSort(arr)
            m_t2 = time.time()
            mergetime = m_t2 - m_t1
            suma_m = suma_m + mergetime


            i_t1 = time.time()
            insertionSort(arr_2)
            i_t2 = time.time()
            inserttime = i_t2 - i_t1
            suma_i = suma_i + inserttime


            t_t1 = time.time()
            timSort(arr_3,20)
            t_t2 = time.time()
            timtime = t_t2 - t_t1
            suma_t = suma_t + timtime


        summma_m.append(100000*suma_m/epochs)
        summma_i.append(100000*suma_i/epochs)
        summma_t.append(100000 * suma_t / epochs)


    return summma_m, summma_i, summma_t

num = 100
epochs  = 1000

summma_m, summma_i, summma_t= test(num, epochs)


def plott(num,summma_m,summma_i,summma_t):
    plt.title('running time for MegeSort, InsertionSort and TimSort')
    plt.plot(range(0,num), summma_m,c = 'r',label = 'merge sort')
    plt.plot(range(0,num),summma_i, c = 'b', label = 'insertion sort')
    plt.plot(range(0,num),summma_t, c = 'g', label = 'tim sort')
    plt.xlabel("Input size (N)")
    plt.ylabel("Scaled Running Time of Algorithm (seconds)")
    plt.legend()
    plt.show()


plott(num,summma_m,summma_i,summma_t)

#References:
# mergesort: https://www.geeksforgeeks.org/merge-sort/
# insertion sort:https://www.runoob.com/python3/python-insertion-sort.html

