class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.parantheses_combination_arr = []
        self.n = n
        self.dfs(0,0,"",0)
        return(self.parantheses_combination_arr)
        
    def dfs(self,count,total_pairs,str,open_brackets):
        
            
        if(total_pairs == self.n):
            self.parantheses_combination_arr.append(str)
            
        elif(count == 0):
                
            if(open_brackets<self.n):
                self.dfs(count+1,total_pairs,str+"(",open_brackets+1)
                
            
        elif(count > 0):
                
            if(open_brackets<self.n):
                self.dfs(count+1,total_pairs,str+"(",open_brackets+1)
                    
            self.dfs(count - 1,total_pairs+1,str + ")", open_brackets)
                
            