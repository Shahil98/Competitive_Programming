class Solution {
public:

    int max(int a,int b)
    {
        if(a>b)
        {
            return(a);
        }
        else
        {
            return(b);
        }
    }

    bool canJump(vector<int>& nums)
    {
        int cur_best = 0;

        if(nums.size() <= 1)
        {
            return(true);
        }

        for(int i=0;i<nums.size()-1;i++)
        {
            cur_best = max(cur_best-1,nums[i]);

            if(cur_best == 0 )
            {
                return(false);
            }

        }

        return(true);

    }

};
