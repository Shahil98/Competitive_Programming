class Solution(object):
    def __init__(self):
        self.arr = [] 
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return(self.perm(nums))
        
    def perm(self,arr):
        if(len(arr)<=1):
            return([arr])
        if(len(arr)==2):
            return([[arr[0],arr[1]],[arr[1],arr[0]]])
        else:
            ans = []
            new_arr = []
            new_arr = arr[:]
            for i in range(len(arr)):
                new_arr.pop(i)
                ans.append(self.perm(new_arr))
                new_arr = arr[:]
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    ans[i][j] = [arr[i]] + ans[i][j]
            new_ans = []
            cnt = len(ans[0])
            for i in range(len(ans)):
                for j in range(cnt):
                    new_ans.append(ans[i][j])
            return(new_ans)
        