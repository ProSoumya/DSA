#Implementation of Binary Search Algorithm 
# Time Complexicty : O(Log N)
# Try to do the binary search algorithm using (Iterative Approaches)

import numpy as np

def binary_search(arr,i,j,x):
    ##Single Element Search
    if i == j:
        if arr[i] == x:
            return i
        else:
            return -1
    else:
        mid = i + (j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr,mid+1,j,x)
        else:
            return binary_search(arr,i,mid-1,x)
        
arr  =  np.array([5, 10, 20, 27, 30, 35, 39, 42])
i = 0
j = len(arr)-1
search_number = 87
result = binary_search(arr,i,j,search_number)
print("Binary Seach Index ",result)