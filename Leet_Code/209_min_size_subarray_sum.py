class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        n = len(nums)
        cur_ans = 999999
        sum = 0
        end = start
        while(end<n and start<=end):
            sum += nums[end]
            #print("start: ",start,"end: ",end,"sum: ",sum)
            if(sum >= s):
                if((end-start+1)<cur_ans):
                    cur_ans = end-start+1
                sum -= nums[start]
                sum -= nums[end]
                start += 1
            else:
                end += 1
        if(cur_ans == 999999):
            cur_ans = 0
        return(cur_ans)