class Solution(object):
    
    def recurse(self, sum, i):
        if((i, sum%3) in self.visited):
            return(self.visited[(i, sum%3)])
        if(i == len(self.nums)):
            if(sum%3 == 0):
                return(sum)
            else:
                return(0)
        res1 = self.recurse(sum+self.nums[i], i+1)
        res2 = self.recurse(sum, i+1)
        self.visited[(i, sum%3)] = max(res1, res2)
        return(self.visited[(i, sum%3)])
    
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        
        first_one = float("inf")
        first_two = float("inf")
        second_one = float("inf")
        second_two = float("inf")
        
        for i in range(len(nums)):
            sum += nums[i]
            if(nums[i]%3 == 1):
                if(first_one > nums[i]):
                    second_one = first_one
                    first_one = nums[i]
                else:
                    second_one = min(second_one, nums[i])
            if(nums[i]%3 == 2):
                if(first_two > nums[i]):
                    second_two = first_two
                    first_two = nums[i]
                else:
                    second_two = min(second_two, nums[i])
        if(sum%3 == 0):
            return(sum)
        elif(sum%3 == 1):
            return(max(sum-first_one, sum-first_two-second_two))
        else:
            return(max(sum-first_two, sum-first_one-second_one))