class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.n = len(word) - 1
        self.word = word
        self.board = board
        
        self.rows = len(self.board)
        self.columns = len(self.board[0])
        
        visited = []
        for i in range(self.rows):
            arr = []
            for j in range(self.columns):
                arr.append(0)
            visited.append(arr)
        for i in range(self.rows):
            for j in range(self.columns):
                if(self.backtrack(i,j,visited,0) == True):
                    return(True)
        return(False)
    def backtrack(self,i,j,visited,count):
        if(count > self.n):
            return(True)
        elif(i<0 or j<0 or i>(self.rows-1) or j>(self.columns-1)):
            return(False)
        elif(visited[i][j]==1):
            ans = False
            pass
        else:
            ans = False
            visited[i][j] = 1
            if(self.word[count] == self.board[i][j]):
                ans = (self.backtrack(i+1,j,visited,count+1) or self.backtrack(i,j+1,visited,count+1) or self.backtrack(i-1,j,visited,count+1) or self.backtrack(i,j-1,visited,count+1))
            visited[i][j] = 0
            return(ans)
            
        return(False)
            
        