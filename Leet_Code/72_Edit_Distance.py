class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        
        self.cache = {}
        return(self.calculateCost(word1,word2,len(word1),len(word2)))
    
    def calculateCost(self,word1,word2,m,n):

        try:
            return(self.cache[(m,n)])
        except:
            if(m == 0 ):
                return(n)
            if(n == 0):
                return(m)
            if(word1[m-1] == word2[n-1]):
                return(self.calculateCost(word1,word2,m-1,n-1))
            else:
                ans = 1 + min(self.calculateCost(word1,word2,m-1,n),self.calculateCost(word1,word2,m,n-1),self.calculateCost(word1,word2,m-1,n-1)) 
                self.cache[(m,n)] = ans
                return(ans)

    

                
                
                
            