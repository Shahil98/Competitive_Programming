class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        nrows = len(grid)-1
        ncolumns = len(grid[0])-1
        
        queue = [(0, 0, k, 0)]
        visited = {}
        min_val = float('inf')
        visited = {}
        visited[(0, 0, k)] = 1
        
        neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        while(queue):
            cur_element = queue.pop(0)
            x = cur_element[0]
            y = cur_element[1]
            k = cur_element[2]
            level = cur_element[3]
            
            if(x == nrows and y == ncolumns):
                return(level)
            
            for (dx, dy) in neighbors:
                
                new_x = x + dx
                new_y = y + dy
                
                key = (new_x , new_y, k)
                
                if((key not in visited) and 0<=new_x<=nrows and 0<=new_y<=ncolumns):
                    
                    visited[key] = 1
                    
                    if(grid[new_x][new_y]==1 and k>0):
                        queue.append((new_x, new_y, k-1, level+1))
                    elif(grid[new_x][new_y]==0):
                        queue.append((new_x, new_y, k, level+1))
                
        return(-1)
    
                
                    
        
        