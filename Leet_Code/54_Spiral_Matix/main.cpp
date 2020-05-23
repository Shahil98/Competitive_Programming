class Solution {
public:
    vector<int> output;


    vector<int> spiralOrder(vector<vector<int>>& matrix)
    {
        if(matrix.size()!=0)
        {
            generateOutput(matrix);
        }

        return(output);
    }

    bool notEven(int n)
    {
        if(n%2 == 0)
        {
            return(false);
        }
        else
        {
            return(true);
        }
    }

    void generateOutput(vector<vector<int>>& matrix)
    {
        int n = matrix.size()/2;
        int top = 0;
        int bottom = matrix.size()-1;
        int left = 0;
        int right = matrix[0].size()-1;
            while((left < right) and (top < bottom))
            {
                for(int j=left;j<=right;j++)
                {
                    output.push_back(matrix[top][j]);
                }
                for(int j=top+1;j<=bottom;j++)
                {
                    output.push_back(matrix[j][right]);
                }
                for(int j=right-1;j>=left;j--)
                {
                    output.push_back(matrix[bottom][j]);
                }
                for(int j=bottom-1;j>top;j--)
                {
                    output.push_back(matrix[j][left]);
                }
                left++;
                top++;
                bottom--;
                right--;
            }


            if((left == right) && (notEven(matrix[0].size())))
            {
                for(int j=top;j<=bottom;j++)
                {
                    output.push_back(matrix[j][left]);
                }
            }
            else if(top == bottom && (notEven(matrix.size())))
            {
                for(int j=left;j<=right;j++)
                {
                    output.push_back(matrix[top][j]);
                }
            }

    }

};
