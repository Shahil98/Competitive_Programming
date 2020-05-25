class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.find_arrays(candidates,target,[])
        return(self.ans)
    def find_arrays(self,candidates,target,arr):
        if(target == 0):
            arr.sort()
            if(arr not in self.ans):
                self.ans.append(arr)
                return(0)
        elif(target > 0 and len(candidates)>0):
            self.find_arrays(candidates[1:],target-candidates[0],arr+[candidates[0]])
            self.find_arrays(candidates[1:],target,arr[:])
        else:
            return(0)