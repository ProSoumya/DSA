import numpy as np

def binary_search(array_1,x):
    low=0
    high = len(array_1) -1
    mid = 0

    while low <= high:
        mid = low  + (high - low)//2

        if array_1[mid] < x:
            low = mid+1
        elif array_1[mid] > x:
            high = mid-1
        else:
            return mid
    return -1
        



arr = np.array([5, 10, 20, 27, 30, 35, 39, 42,45])
result = binary_search(arr,30)
print("Search item is present at index", result)




















