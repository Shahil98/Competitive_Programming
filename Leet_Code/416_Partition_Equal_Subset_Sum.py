class Solution(object):
    
    def recurse(self, i, remaining_capacity):
        
        if((i, remaining_capacity) in self.visited):
            return(self.visited[(i, remaining_capacity)])
        
        if(remaining_capacity == 0):
            return(True)
        elif(i==len(self.nums) or remaining_capacity<0):
            return(False)
        else:
            res1 = self.recurse(i+1, remaining_capacity - self.nums[i])
            if(res1 == True):
                return(True)
            res2 = self.recurse(i+1, remaining_capacity)
            
            res = res1 + res2
            
            self.visited[(i, remaining_capacity)] = res
            
            return(res)
    
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum = 0
        self.nums = nums
        self.visited = {}
        for i in range(len(nums)):
            sum += nums[i]
        
        if(sum%2 != 0):
            return(False)
        else:
            self.target = sum//2
            return(self.recurse(0, self.target))