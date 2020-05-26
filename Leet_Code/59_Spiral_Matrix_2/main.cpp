class Solution {
public:
    vector<vector<int>> generateMatrix(int n)
    {

        if(n==0)
        {
            vector<vector<int>> matrix_vector;
            return(matrix_vector);
        }

        int matrix[n][n];

        int top = 0;
        int left = 0;
        int bottom = n-1;
        int right = n-1;

        int val = 1;

        for(int i = int(n/2); i>0; i--)
        {
            for(int j=left; j<=right; j++)
            {
                matrix[top][j] = val;
                val++;
            }

            for(int j=top+1; j<=bottom; j++)
            {
                matrix[j][right] = val;
                val++;
            }

            for(int j=right-1; j>=left; j--)
            {
                matrix[bottom][j] = val;
                val++;
            }

            for(int j=bottom-1; j>=(top+1); j--)
            {
                matrix[j][left] = val;
                val++;
            }

            top++;
            bottom--;
            left++;
            right--;
        }

        if(n%2 != 0)
        {
            matrix[int(n/2)][int(n/2)] = n*n;
        }

        vector<vector<int>> matrix_vector;

        for(int i=0; i<n; i++)
        {
            //vector<int> temp_vector;

            matrix_vector.push_back(vector<int>(0));

            for(int j=0; j<n; j++)
            {
                matrix_vector[i].push_back(matrix[i][j]);
            }


        }

        return(matrix_vector);
    }
};
