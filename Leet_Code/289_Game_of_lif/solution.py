class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        n_rows = len(board)
        n_columns = len(board[0])
        
        for i in range(n_rows):
            for j in range(n_columns):
                ele = board[i][j]
                alive_neighbours = 0
                for row in range(i-1,i+2):
                    for column in range(j-1,j+2):
                        if(row>=0 and column>=0 and row<n_rows and column<n_columns and (board[row][column]==1 or board[row][column]==-1)):
                            if(not(row==i and column==j)):
                                alive_neighbours += 1
                if(ele == 0):
                    if(alive_neighbours == 3):
                           board[i][j] = 2
                else:
                    if(not(alive_neighbours==2 or alive_neighbours==3)):
                           board[i][j] = -1
        for i in range(n_rows):
            for j in range(n_columns):
                if(board[i][j]==-1):
                    board[i][j] = 0
                elif(board[i][j] == 2):
                    board[i][j] = 1
        return(board)