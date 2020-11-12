class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ans = 2
        while(ans < n):
            ans = ans*2
        ans = ans//2
        print(ans)
        if(ans > m):
            return(0)
    
        else:
            ans = m
            for i in range(m+1, n+1):
                ans = ans&i
            return(ans)
        