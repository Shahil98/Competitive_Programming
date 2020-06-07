class Solution:
    
    def common_substrings(self,string1,string2,n):

        rows = len(string1)
        columns = len(string2)

        self.dp = []

        for i in range(rows):
            arr = []
            for j in range(columns):
                arr.append(0)
            self.dp.append(arr)
        
        self.cur_candidate_i = -1
        self.cur_candidate_val = 0

        for i in range(rows):
            for j in range(columns):
                if(string1[i]==string2[j]):
                    if(i==0 or j==0):
                        self.dp[i][j] = 1
                    else:
                        self.dp[i][j] = 1 + self.dp[i-1][j-1]
                    if( (self.cur_candidate_val < self.dp[i][j])):
                        
                        str1 = string1[i-self.dp[i][j] + 1 : i+1]
                        str2 = str1[::-1]
                        if(str1 == str2):
                            self.cur_candidate_i = i
                            self.cur_candidate_val = self.dp[i][j]
    
    def longestPalindrome(self,s:str) -> str :
        
        reversed_s = ""
        n = len(s)
        
        for i in range(n):
            reversed_s = reversed_s + s[n - i -1]
        
        self.common_substrings(s,reversed_s,n)
        
        ans = ""
        while(self.cur_candidate_val != 0):
            ans = ans + s[self.cur_candidate_i]
            self.cur_candidate_val -= 1
            self.cur_candidate_i -= 1
        return(ans)
