class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triplets = []
        cache = {}
        for i in range(len(nums) - 2):
            
            target_sum = 0 - nums[i]
            
            left = i+1
            right = len(nums)-1
            while(left < right):
                if(nums[left]+nums[right] == target_sum):
                    try:
                        cache[(nums[i],nums[left],nums[right])]
                    except:
                        cache[(nums[i],nums[left],nums[right])] = 1
                        triplets.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif(nums[left]+nums[right] < target_sum):
                    left += 1
                else:
                    right -= 1
        return(triplets)
                    