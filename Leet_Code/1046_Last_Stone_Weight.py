class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        for i in range(len(stones)):
            stones[i] = 0 - stones[i]
        
        heapq.heapify(stones)
        while(True):
            if(len(stones) == 1):
                return(0-stones[0])
            if(len(stones) == 0):
                return(0)
            cur_element = heapq.heappop(stones)
            next_element = heapq.heappop(stones)
            new_element = 0 - (next_element - cur_element)
            if(new_element != 0):
                heapq.heappush(stones, new_element)
            