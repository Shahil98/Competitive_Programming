class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        flag_i = 0
        flag_j = 0
        if(rows != 0 and columns != 0):
            for i in range(rows):
                for j in range(columns):
                    if(matrix[i][j]==0):
                        matrix[0][j] = 0
                        matrix[i][0] = 0
                        if(i == 0):
                            flag_i = 1
                        if(j==0):
                            flag_j = 1
        
            for j in range(1,columns):
                if(matrix[0][j] == 0):
                    for i in range(rows):
                        matrix[i][j] = 0
                    
            for i in range(1,rows):
                if(matrix[i][0] == 0):
                    for j in range(columns):
                        matrix[i][j] = 0
            if(matrix[0][0] == 0):
                if(flag_j == 1):
                    for i in range(rows):
                        matrix[i][0] = 0
                if(flag_i == 1):
                    for j in range(columns):
                        matrix[0][j] = 0
                    