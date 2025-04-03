import random
from sys import setrecursionlimit
import time

def selectionSort(arr):

    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    
    return arr
        
#graded function
def insertionSort(arr):
    
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr
    
def mergeSort(arr, left, right):
    
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
        
    return arr

#helper function for mergeSort
#mid is last element of left array
def merge(arr, left, mid, right):
    
    len1 = mid - left + 1
    len2 = right - mid
    L = [0] * len1
    R = [0] * len2
    for i in range(len1):
        L[i] = arr[left + i]
    for j in range(len2):
        R[j] = arr[mid + 1 + j]
        
    
    i, j, k = 0, 0, left
    while i < len1 and j < len2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1 
    
    while i < len1:
        arr[k] = L[i]
        k += 1
        i += 1
    while j < len2:
        arr[k] = R[j]
        k += 1
        j += 1
        
        
#graded function
def quickSort(arr, left, right):
    
    if left < right:
        #print(arr)
        pivotIndex = partition(arr, left, right)
        
        quickSort(arr, left, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, right)
    
    return arr
        
#helper function for quickSort
def partition(arr, left, right):
    
    #picks the last element as pivot
    pivot = arr[right] 
    i = left
    
    #don't go through right-1 because right is the pivot
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    #swap the pivot with the element at index i 
    #(in between the two partitions)
    arr[i], arr[right] = arr[right], arr[i]
    
    #return the index of the pivot
    return i 



def isSorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def medianOfThree(a, b, c):
    if a < c:
        if b < a:
            return a
        elif c < b:
            return c
        else:
            return b
    elif b < c:
        return c
    elif a < b:
        return a
    return b


def main(arrayType = "r", n = 10, algo = "q"):
      
    
    if not arrayType or not (arrayType == "r" or arrayType == "s" or arrayType == "c"):
        print("Invalid Array Type. Using default random array of length ", n)
        arrayType = "r"
    if not algo or not (algo == "q" or algo == "i" or algo == "s" or algo == "m"):
        print("Invalid Sorting Algorithm. Using default Quick Sort")
        algo = "q"
    if not n or n <= 0:
        print("Number of elements in array must be positive and greater than zero. Using default length ", 10)
        n = 10
        
    print("Array Type: ", arrayType, " Array Length: ", n, " Algo: ", algo)
    
    if arrayType == "r":
        arr = [i+1 for i in range(n)]
        random.shuffle(arr)
    elif arrayType == "s":
        arr = [i+1 for i in range(n)]
    elif arrayType == "c":
        arr = [0 for _ in range(n)]
        
    
    #important to copy array for each trial to avoid sorting a sorted array for random array
    totalTime = []
    for i in range(3):
        arrCopy = arr[:]
        startTime = time.time_ns()
        if algo == "s":
            output = selectionSort(arrCopy)
        elif algo == "i":
            output = insertionSort(arrCopy)
        elif algo == "m":
            output = mergeSort(arrCopy, 0, n - 1)
        elif algo == "q":
            output = quickSort(arrCopy, 0, n - 1)
        endTime = time.time_ns()
        totalTime.append(endTime - startTime)
        
        if not isSorted(output):
            print("Your solution algorithm failed.")
            for j in range(len(output)):
                print(output[j], end = " ")
            break

    else:
        print("Median Execution Time: ", medianOfThree(totalTime[0], totalTime[1], totalTime[2]), " ns")
        
#run the four sorting algorithms on constant, sorted, and random arrays that are powers of 10
#run on the following:
#1. Nmin: the smallest power of 10 array size that takes 20 milliseconds or more per run to sort
#2. Nmax: the largest power of 10 array size that takes 10 minutes or less per run to sort
#Record Nmin, Nmax, Tmin, Tmax


''' Test selectionSort '''

#N^2
main("c", 10000, "s")
main("c", 100000, "s")

#N^2
main("s", 10000, "s")
main("s", 100000, "s")

#N^2
main("r", 10000, "s")
main("r", 100000, "s")

''' Test insertionSort '''

#N
main("c", 1000000, "i")
main("c", 100000000, "i")

#N
main("s", 1000000, "i")
main("s", 100000000, "i")

#N^2
main("r", 10000, "i")
main("r", 100000, "i")

''' Test mergeSort '''

#NlogN
main("c", 10000, "m")
main("c", 10000000, "m")

#NlogN
main("s", 10000, "m")
main("s", 10000000, "m")

#NlogN
main("r", 10000, "m")
main("r", 10000000, "m")

''' Test quickSort '''

#change max recursion depth
setrecursionlimit(1000000)

#N^2 (depends on pivot)
main("c", 10000, "q")
main("c", 100000, "q")

#N^2 (depends on pivot)
main("s", 10000, "q")
main("s", 100000, "q")

#NlogN 
main("r", 10000, "q")
main("r", 10000000, "q")