"""
    O(n^2)  Time complexity
    O(1) - Space complexity
    This is useful when we require least amount of swap
    Comparision - O(n^2) 
    Swaping - O(n) 

"""
def selectionsort1darray(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j


        arr[i],arr[min_index] = arr[min_index],arr[i] 
    return arr


if __name__ == '__main__':
    array_sort=[50,25,38,44,99,16,11,21]
    result = selectionsort1darray(array_sort)
    print(f"Sorted Attay is : {result}")