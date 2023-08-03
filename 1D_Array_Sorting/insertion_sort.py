"""
    O(n^2)  Time complexity  for Worst Case and O(n) for Best case scenario
    O(1) Space Complexity
    This is useful when the input array is almost sorted
"""

def insertionsort(arr):
    for i in range(1,len(arr)):
        value = arr[i]
        j=i-1

        while (j>=0 and value < arr[j]):
            arr[j+1] = arr[j]
            j-=1
        
        arr[j+1] = value
    return arr



if __name__ == '__main__':
    arr = [75,90,100,95,85,50,110,7]
    result = insertionsort(arr)
    print(f"Result after Insertionsort : {result}") 