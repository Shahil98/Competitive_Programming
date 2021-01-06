class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.wordDict = wordDict
        self.cache = {}
        return(self.dfs(s))
        
    def dfs(self, st):
        if(st == ""):
            return(True)
        else:
            
            if(st in self.cache):
                return(self.cache[st])
            result = False
            for i in range(1,len(st)+1):
                segment1 = st[:i]
                if(segment1 in self.wordDict):
                    result = self.dfs(st[i:])
                if(result == True):
                    self.cache[st] = True
                    return(True)
            self.cache[st] = False
            return(False)