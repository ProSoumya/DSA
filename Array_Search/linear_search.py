## Time Complexcity : O(n) 
import numpy as np

def linear_search(array_1,n,search_element):
    for i in range(n):
        if array_1[i] == search_element:
            return i
    ##Element is not found in the array_1 
    return -1

array_1 = np.array([13, 56, 67, 78, 96, 75, 32])
n = len(array_1) 
search_element = 78
result = linear_search(array_1, n, search_element)
print("Search element index is ", result)