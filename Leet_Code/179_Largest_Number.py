class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                st1 = int(nums[i]+nums[j])
                st2 = int(nums[j]+nums[i])
                if(st1<st2):
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        ans = ""
        for i in range(len(nums)):
            ans = ans + nums[i]
        if(len(ans)>1):
            i = 0
            while(ans[i]=="0" and len(ans)>1):
                ans = ans[1:]
        return(ans)
        