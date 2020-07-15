class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []
        self.permute(nums[:],[])
        return(self.subsets)
    def permute(self,nums,arr):
        if(len(nums)==0):
            self.subsets.append(arr)
            return 0
        else:
            if(len(arr)!=0):
                self.permute(nums[1:],arr[:])
            else:
                self.permute(nums[1:],[])
            arr.append(nums[0])
            self.permute(nums[1:],arr[:])