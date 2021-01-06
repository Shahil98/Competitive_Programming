class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        count = 0
        max_ans = 0
        for i in range(len(nums)):
            if(nums[i]==0):
                count -= 1
            else:
                count += 1
            if(count == 0):
                max_ans = i+1
            elif(count in dict):
                max_ans = max(max_ans, i-dict[count])
            else:
                dict[count] = i
                
        return(max_ans)