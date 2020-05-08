class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.find_arrays(0,candidates,target,[])
        return(self.ans)
    def find_arrays(self,start,candidates,target,arr):
        if(target == 0):
            #arr.sort()
            #if(arr not in self.ans):
            self.ans.append(arr)
            return(0)
        elif(target > 0):
            for i in range(start,len(candidates)):
                self.find_arrays(i,candidates,target-candidates[i],arr+[candidates[i]])
        else:
            return(0)