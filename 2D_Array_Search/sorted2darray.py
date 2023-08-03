'''
            Task : Search for a Target value in a Given  2D matrix and get the index for that Target value.

            Given : The Matrix is sorted in both Row and columns (In ascending order)

            Requirement : Solving this within O(n) Time Complexity 

'''
def search2dmatrix(matrix,target):
    i = 0
    j= len(matrix[0])-1  # no of columns in the matrix
    n = len(matrix)      #no of rows in the matrix
    while (i<n and j>=0) :
        print("Searching for")    
        if matrix[i][j] == target:
            return [i,j]
        elif (matrix[i][j] > target):
            j-=1
        else:
            i+=1
    return [-1,-1]
    
mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target =12
result = search2dmatrix(mat,target)
print(f"Result is {result}")