class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = [(amount,0)]
        visited = {}
        
        if(amount == 0):
            return(0)
        
        while(queue):
            new_amount = queue[0]
            queue.pop(0)
            
            for coin in coins:
                decreased_amount = (new_amount[0]-coin, new_amount[1]+1)
                if(decreased_amount[0] == 0):
                    return(decreased_amount[1])
                elif((decreased_amount[0] not in visited) and (decreased_amount[0]>0)):
                    queue.append(decreased_amount)
                    visited[decreased_amount[0]] = 1
        return(-1)
                    
        