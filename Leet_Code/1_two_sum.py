class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)

        if(n<2):
            return([])

        dictionary_of_numbers_seen = {}
        dictionary_of_numbers_seen[nums[0]] = 0

        for i in range(1,n):
            try:
                j = dictionary_of_numbers_seen[target-nums[i]]
                return([j, i])
            except:
                dictionary_of_numbers_seen[nums[i]] = i
                