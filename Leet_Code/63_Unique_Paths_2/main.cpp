class Solution {
public:

    int final_i;
    int final_j;
    vector<vector<int>> cache;

    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid)
    {
        final_i = obstacleGrid.size()-1;
        final_j = obstacleGrid[0].size()-1;

        if((final_i+1)==0 || (final_j+1)==0)
        {
            return(1);
        }

        if(obstacleGrid[0][0]==1)
        {
            return(0);
        }

        for(int i=0; i<=final_i; i++)
        {
            cache.push_back(vector<int>());
            for(int j=0; j<=final_j; j++)
            {
                cache[i].push_back(-1);
            }
        }

        if(obstacleGrid[final_i][final_j]==1 || obstacleGrid[0][0]==1)
        {
            return(0);
        }

        return(dfs(obstacleGrid,0,0));
    }

    int dfs(vector<vector<int>>& obstacleGrid, int i, int j)
    {
        if(i==final_i && j==final_j)
        {
            return(1);
        }

        else
        {
            int ans1 = 0;
            int ans2 = 0;

            if(i<=final_i && j<final_j)
            {
                if(cache[i][j]!=(-1))
                {
                    return(cache[i][j]);
                }

                if(obstacleGrid[i][j+1]!=1)
                {
                    ans1 = dfs(obstacleGrid, i, j+1);
                }
            }

            if(i<final_i && j<=final_j)
            {
                if(cache[i][j]!=(-1))
                {
                    return(cache[i][j]);
                }

                if(obstacleGrid[i+1][j]!=1)
                {
                    ans2 = dfs(obstacleGrid, i+1, j);
                }
            }

            if(i<=final_i && j<=final_j)
            {
                cache[i][j] = ans1 + ans2;
            }

            return(ans1+ans2);


        }
    }
};
