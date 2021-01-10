class Solution(object):
    
    def recurse(self, i, sum):
        
        if((i, sum) in self.visited):
            return(self.visited[(i, sum)])
        if(i == len(self.nums)):
            if(sum == self.S):
                return(1)
            else:
                return(0)
        else:
            res1 = self.recurse(i+1, sum+self.nums[i])
            res2 = self.recurse(i+1, sum-self.nums[i])
            self.visited[(i, sum)] = res1 + res2
            return(res1+res2)
    
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.nums = nums
        self.visited = {}
        self.S = S
        return(self.recurse(0, 0))