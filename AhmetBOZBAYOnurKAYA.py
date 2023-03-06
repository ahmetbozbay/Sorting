#Ahmet Bozbay 150119861
#Onur Kaya 150119860
import random
from time import process_time
import sys
sys.setrecursionlimit(10000) # Not take for that error : RecursionError: maximum recursion depth exceeded in comparison
randomlist = [] # The numbers generated will be transferred to this list.
insertionSortlist = [] # The numbers generated will be transferred to this list. For insertionSortlist
MergeSortlist=[] # The numbers generated will be transferred to this list. For MergeSortlist
QuickSortlist=[] # The numbers generated will be transferred to this list. For QuickSortlist
PartialSelectionlist=[] # The numbers generated will be transferred to this list. For PartialSelectionSortlist
HeapSort=[]  # The numbers generated will be transferred to this list. For HeapSortlist
QuickSelectAlgorithm=[]   # The numbers generated will be transferred to this list. For QuickSelectAlgorithm
k=int(input("Select the k'th term :")) # To decide which term to give.
for i in range(0,3000): # to determine how many numbers we will generate.
    n = random.randint(1,100000) # to determine between which number values we will generate.
    randomlist.append(n) # to add the generated numbers to the list.
    insertionSortlist.append(n)  # to add the generated numbers to the list.
    MergeSortlist.append(n)  # to add the generated numbers to the list.
    QuickSortlist.append(n)  # to add the generated numbers to the list.
    PartialSelectionlist.append(n)   # to add the generated numbers to the list.
    HeapSort.append(n)   # to add the generated numbers to the list.
    QuickSelectAlgorithm.append(n)   # to add the generated numbers to the list.
randomlist = list(dict.fromkeys(randomlist)) #to delete the same values if the generated values are the same.
print(str(len(randomlist)) + " times random numbers are generated. \nGenerated list is : ")
print(randomlist) #Printing Generated randomlist
insertionSortlist = list(dict.fromkeys(randomlist)) #to delete the same values if the generated values are the same.
MergeSortlist = list(dict.fromkeys(randomlist)) #to delete the same values if the generated values are the same.
QuickSortlist = list(dict.fromkeys(randomlist)) #to delete the same values if the generated values are the same.
PartialSelectionlist = list(dict.fromkeys(randomlist)) #to delete the same values if the generated values are the same.
HeapSort = list(dict.fromkeys(randomlist)) #to delete the same values if the generated values are the same.
QuickSelectAlgorithm = list(dict.fromkeys(randomlist)) #to delete the same values if the generated values are the same.
t1_start = process_time()
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key
insertionSort(insertionSortlist)
print('\nInsertion Sorted Array in Ascending Order:')
print(insertionSortlist) # Printing list
print(str(k)+"'th element is "+ str(insertionSortlist[k-1]))
t1_stop = process_time()
print("Insertion sort process takes ", t1_stop)
t2_start = process_time()
def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
array = MergeSortlist
mergeSort(array)
print("\nMerge Sorted array is: ")
print(array) # Printing list
print(str(k)+"'th element is "+ str(array[k-1]))
t2_stop = process_time()
print("Merge sort process takes ", t2_stop-t1_stop)
# function to find the partition position
t3_start = process_time()
def partition(array, low, high):

  # choose the first element as pivot
  pivot = array[0]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)

data = QuickSortlist
size = len(data)
quickSort(data, 0, size - 1)
print('\nQuick Sorted Array in Ascending Order:')
print(data) # Printing list
print(str(k)+"'th element is "+ str(data[k-1]))
t3_stop = process_time()
print("Quick sort process takes ", t3_stop-t2_stop)
t4_start = process_time()

def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
data = PartialSelectionlist
size = len(data)
selectionSort(data, size)
print('\nPartial Selection Sorted Array in Ascending Order:')
print(data) # Printing list
a=(data[0]) # Taking first element of Insertionlist
print("Smallest element is "+str(data[0])+".\n" +str(data[0]) +"th element is :" + str(data[a-1]))
t4_stop = process_time()
print("Partial Selection Sort process takes ", t4_stop-t3_stop)
t5_start = process_time()
def heapify(arr, n, i):
    # Find largest among root and children
    maxheap = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        maxheap = l

    if r < n and arr[maxheap] < arr[r]:
        maxheap = r

    # If root is not largest, swap with largest and continue heapifying
    if maxheap != i:
        arr[i], arr[maxheap] = arr[maxheap], arr[i]
        heapify(arr, n, maxheap)

def heapSort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)

arr = HeapSort
heapSort(arr)
n = len(arr)
print("\nHeap Sorted array is")
print(arr) # Printing list

for i in range(0,k):
    arr=arr[:-1]     # The for loop required to delete up to k'th
print("n-k times max removal is ")
print(arr) # Printing list
print("Max element is "+ str(arr[-1])) # The rightmost value of the remaining list is the largest value of the list.
t5_stop = process_time()
print("Partial Heap Sort process takes ", t5_stop-t4_stop)
t6_start = process_time()

# Standard partition process of QuickSort().
# It considers the last element as pivot
# and moves all smaller element to left of
# it and greater elements to right
def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):

        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i
arr = QuickSelectAlgorithm
t6_stop = process_time()
print("\nQuick Select Sort array is")
print(arr)
a=QuickSelectAlgorithm[0]
print("Pivot index is : " + str(a))
print("Quick Select Sort process takes ", t6_stop-t5_stop)
