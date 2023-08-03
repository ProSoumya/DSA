# Time Complexity is O(n^2)

def linear_search(matrix,num):   # Time complexity is O(n) * O(n) => O(n^2)
    for i in range(len(matrix)): #O(n)
        for j in range(len(matrix[i])): #(O(n))
            # print(matrix[i,j])
            if (matrix[i][j] == num):
                # print(f"Index of Item is {i,j}")
                return [i,j]
    return [-1,-1]

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
num_search = 12
result = linear_search(mat,num_search)  
print("Index of Item is",[result[0],result[1]])