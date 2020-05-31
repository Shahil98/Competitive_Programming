class Solution {
public:

    vector<vector<int>> gridRectangle;
    int final_i = 0;
    int final_j = 0;
    vector<vector<int>> cache;


    int minPathSum(vector<vector<int>>& grid)
    {
        gridRectangle = grid;

        if(grid.size()==0 || grid[0].size()==0)
        {
            return(0);
        }

        final_i = grid.size()-1;
        final_j = grid[0].size()-1;

        for(int i=0; i<=final_i; i++)
        {
            cache.push_back(vector<int>());

            for(int j=0; j<=final_j; j++)
            {
                cache[i].push_back(-1);
            }
        }

        return(dfs(0,0));
    }

    int dfs(int i,int j)
    {
        if(cache[i][j] != -1)
        {
            return(cache[i][j]);
        }

        if(i == final_i && j == final_j)
        {
            return(gridRectangle[i][j]);
        }

        int ans1 = -1;
        int ans2 = -1;

        if(i==final_i)
        {
            cache[i][j] = gridRectangle[i][j] + dfs(i,j+1);
            return(cache[i][j]);
        }

        else if(j == final_j)
        {
            cache[i][j] = gridRectangle[i][j] + dfs(i+1,j);
            return(cache[i][j]);
        }

        else
        {
            int ans1 = gridRectangle[i][j] + dfs(i+1,j);
            int ans2 = gridRectangle[i][j] + dfs(i,j+1);

            if(ans1 < ans2)
            {
                cache[i][j] = ans1;
                return(ans1);
            }

            else
            {
                cache[i][j] = ans2;
                return(ans2);
            }
        }

    }
};
