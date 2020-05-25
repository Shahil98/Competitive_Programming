class Solution {
public:

    map<int,int> cache;

    bool canReach(vector<int>& arr, int start)
    {
        int n = arr.size();

        for(int i=0;i<n;i++)
        {
            cache[i] = 0;
        }

        cache[start] = 1;

        return(dfs(arr,start,n));
    }

    bool dfs(vector<int>& arr, int index, int n)
    {
        if(arr[index]==0)
        {
            return(true);
        }
        else
        {
            int forward = index + arr[index];
            int backward = index - arr[index];

            if(forward < n)
            {
                if(cache[forward] == 0)
                {
                    cache[forward] = 1;
                    bool ans = dfs(arr,forward,n);
                    if(ans == true)
                    {
                        return(true);
                    }
                }
            }

            if(backward >= 0)
            {
                if(cache[backward] == 0)
                {
                    cache[backward] = 1;
                    bool ans = dfs(arr,backward,n);
                    if(ans == true)
                    {
                        return(true);
                    }
                }
            }

            return(false);
        }
    }
};
