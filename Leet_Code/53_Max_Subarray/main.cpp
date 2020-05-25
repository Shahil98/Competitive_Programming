class Solution {
public:

    int max(int a, int b){
        if(a>b){
            return(a);
        }
        else{
            return(b);
        }
    }

    int maxSubArray(vector<int>& nums) {

        int cur_sum = nums[0];
        int max_sum = nums[0];
        if(nums.size()==1){
            return(max_sum);
        }
        else{
            for(int i=1; i<nums.size();i++){
                cur_sum = max(cur_sum+nums[i],nums[i]);
                max_sum = max(cur_sum,max_sum);
            }
            return(max_sum);
        }
    }
};
