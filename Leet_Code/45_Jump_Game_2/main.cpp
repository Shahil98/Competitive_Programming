class Solution {
public:
    int jump(vector<int>& nums) {

        if(nums.size()<=1)
        {
            return(0);
        }

        int cur_pos = 0;
        int buffer = 0;
        int ans = 0;

        while(cur_pos != (nums.size()-1))
        {
            pair<int,int> best(-1,-1);
            for(int i=(cur_pos+buffer+1);i<=(cur_pos+nums[cur_pos]);++i)
            {

                if(i==(nums.size()-1))
                {
                    cur_pos = i;
                    ans++;
                    return(ans);
                }

                if(best.second < (i+nums[i]))
                {
                    best.first = i;
                    best.second = i + nums[i];
                }
            }

            buffer = cur_pos + nums[cur_pos] - best.first;
            cur_pos = best.first;

            ans++;
        }

        return(ans);
    }
};
