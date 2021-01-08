class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = 0
        j = len(matrix[0])-1
        
        while(i>=0 and i<len(matrix) and j>=0 and j<len(matrix[0])):
            if(matrix[i][j]==target):
                return(True)
            elif(matrix[i][j]<target):
                i += 1
            else:
                j -= 1
        return(False)
            