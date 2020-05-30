class Solution {
public:

    vector<vector<int>> cache;
    vector<vector<int>> gridRectangle;
    int rows;
    int columns;
    int validSquares = 0;

    int uniquePathsIII(vector<vector<int>>& grid)
    {
        vector<vector<int>> visited;

        rows = grid.size();
        columns = grid[0].size();

        if(rows==0 || columns == 0)
        {
            return(1);
        }

        gridRectangle = grid;

        int start_i=0, start_j=0;

        for(int i=0; i<rows; i++)
        {
            cache.push_back(vector<int>());
            visited.push_back(vector<int>());
            for(int j=0; j<columns; j++)
            {
                cache[i].push_back((-1));
                visited[i].push_back((0));
                if(grid[i][j] == 1)
                {
                    start_i = i;
                    start_j = j;
                }
                if(grid[i][j]!=(-1))
                {
                    validSquares++;
                }
            }
        }

        if(validSquares == 0)
        {
            return(0);
        }

        return(dfs(start_i,start_j,visited,0));
    }

    int dfs(int i,int j,vector<vector<int>> visited,int count)
    {
        visited[i][j] = 1;
        count++;

        //if(cache[i][j] != (-1))
        //{
         //   return(cache[i][j]);
        //}

        if(gridRectangle[i][j] == 2)
        {
            visited[i][j] = 1;
            if(count == validSquares)
                return(1);
            else
                return(0);
        }

        if(gridRectangle[i][j] == -1)
        {
            visited[i][j] = 1;
            return(0);
        }

        int ans1 = 0, ans2 = 0, ans3 = 0, ans4 = 0;

        if((i+1)<rows && j<columns && j>=0)
        {
            if(visited[i+1][j]!=1)
                ans1 = dfs(i+1,j,visited,count);
        }

        if((i-1)>=0 && j<columns && j>=0 )
        {
            if(visited[i-1][j]!=1)
                ans2 = dfs(i-1,j,visited,count);
        }

        if((j+1)<columns && i<rows && i>=0)
        {
            if(visited[i][j+1]!=1)
                ans3 = dfs(i,j+1,visited,count);
        }

        if((j-1)>=0 && i<rows && i>=0 )
        {
            if(visited[i][j-1]!=1)
                ans4 = dfs(i,j-1,visited,count);
        }

        int ans = ans1 + ans2 + ans3 + ans4;
        //cache[i][j] = ans;
        return(ans);
    }
};
