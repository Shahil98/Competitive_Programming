class Solution(object):
    def __init__(self):
        self.matrix = [[]]
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        comp = 0
        self.matrix = grid
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if(self.matrix[i][j]=="1"):
                    self.cal_comp(i,j)
                    comp = comp + 1
        return(comp)
    
    def cal_comp(self,i,j):
        if(i<len(self.matrix) and j<len(self.matrix[0]) and i>=0 and j>=0):
            #print(i,j)
            #print(len(self.matrix),(self.matrix[0]))
            if(self.matrix[i][j]=="1"):
                self.matrix[i][j] = "2"
                self.cal_comp(i+1,j)
                self.cal_comp(i,j+1)
                self.cal_comp(i-1,j)
                self.cal_comp(i,j-1)
                return(0)
            else:
                return(0)
        else:
            return(0)