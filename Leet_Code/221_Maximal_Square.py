class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        max_val = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if((i-1)>=0 and (j-1)>=0):
                    if(matrix[i][j] == 1):
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + matrix[i][j]
                        if(matrix[i][j] > max_val):
                            max_val = matrix[i][j]
                else:
                    if(matrix[i][j] > max_val):
                        max_val = matrix[i][j]
        return(max_val*max_val)