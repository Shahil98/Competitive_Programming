class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return(0)
        return(self.cal_peak(nums,1,len(nums)))
    
    def cal_peak(self,nums,i,j):
        mid = (i+j)//2 - 1
        if(len(nums) == 1):
            return(0)
        else:
            if((mid+1)>(len(nums)-1)):
                next_ = nums[mid] - 1
            else:
                next_ = nums[mid + 1]
            if((mid-1)<0):
                prev_ = nums[mid]-1
            else:
                prev_ = nums[mid-1]
            if(prev_<nums[mid] and next_<nums[mid]):
                return(mid)
            else:
                if(prev_>nums[mid]):
                    return(self.cal_peak(nums,i,mid))
                else:
                    return(self.cal_peak(nums,mid+2,j))