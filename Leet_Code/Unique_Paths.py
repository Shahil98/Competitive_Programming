class Solution(object):
    def __init__(self):
        self.Matrix = []
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = []
        for i in range(m):
            arr = []
            for j in range(n):
                arr.append(0)
            matrix.append(arr)
        self.Matrix = matrix
        return(self.cal_uniquePaths(m,n,1,1))
    
    def cal_uniquePaths(self,m,n,i,j):
        if(j==n):
            return(1)
        elif(i==m):
            return(1)
        else:
            if(self.Matrix[i][j]!=0):
                return(self.Matrix[i][j])
            ans = (self.cal_uniquePaths(m,n,i+1,j) + self.cal_uniquePaths(m,n,i,j+1))
        self.Matrix[i][j] = ans
        return(ans)
        
        