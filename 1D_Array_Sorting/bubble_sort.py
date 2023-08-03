"""
    O(n^2)  Time complexity
    O(1) Space Complexity
    This is useful when we require least amount of swap
    Comparision - O(n^2) 
    Swaping - O(n^2) 

"""

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            
    
    return arr


if __name__ == "__main__":
    arr = [70,20,50,30,90,5,15]
    result = bubblesort(arr)
    print(f"Sorted Array after Bubble Sort : {result}")

