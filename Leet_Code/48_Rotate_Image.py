class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if(i<j):
                    temp = matrix[i][j] 
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        i = 0
        j = len(matrix)-1
        while(i<j):
            for k in range(len(matrix)):
                temp = matrix[k][i] 
                matrix[k][i] = matrix[k][j]
                matrix[k][j] = temp
            i = i + 1
            j = j - 1
        return(matrix)