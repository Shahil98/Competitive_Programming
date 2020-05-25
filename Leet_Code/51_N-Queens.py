class Solution(object):
    def solveNQueens(self, n):
        self.final_arr = []
        self.n = n
        pos = [-1 for i in range(self.n)]
        arr = []
        for i in range(self.n):
            row = ""
            for j in range(self.n):
                row = row + "."
            arr.append(row)
        self.dfs(arr[:],0,pos[:])
        return(self.final_arr)

    def dfs(self,arr,i,pos):
        for j in range(self.n):
            row = ""
            for k in range(self.n):
                if(k==j):
                    row = row + "Q"
                else:
                    row = row + "."
            arr[i] = row
            pos[i] = j
            isValid = self.check_validity(arr[:],pos[:],i)
            if(isValid==True):
                if(i==((self.n)-1)):
                    self.final_arr.append(arr[:])
                else:
                    self.dfs(arr[:],i+1,pos[:])
    
    def check_validity(self,arr,pos,i):
        for k in range(i):
            if(pos[k]==pos[i]):
                return(False)
            elif(abs(pos[i]-pos[k]) == abs(i-k)):
                return(False)
        return(True)


    