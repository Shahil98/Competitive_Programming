import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap_for_large_nums = []
        self.max_heap_for_small_nums = []
        self.len_min_heap = 0
        self.len_max_heap = 0
        
    def addNum(self, num: int) -> None:
        if(self.len_max_heap == 0):
            heapq.heappush(self.max_heap_for_small_nums,-num)
            self.len_max_heap += 1
        elif(self.len_max_heap > self.len_min_heap):
            if((-self.max_heap_for_small_nums[0]) < (num)):
                heapq.heappush(self.min_heap_for_large_nums,num)
                self.len_min_heap += 1
            else:
                heapq.heappush(self.min_heap_for_large_nums,-heapq.heappop(self.max_heap_for_small_nums))
                heapq.heappush(self.max_heap_for_small_nums,-num)
                self.len_min_heap += 1
        elif(self.len_max_heap == self.len_min_heap):
            if(self.min_heap_for_large_nums[0] < num):
                heapq.heappush(self.max_heap_for_small_nums,-heapq.heappop(self.min_heap_for_large_nums))
                heapq.heappush(self.min_heap_for_large_nums,num)
                self.len_max_heap += 1
            else:
                heapq.heappush(self.max_heap_for_small_nums,-num)
                self.len_max_heap += 1
                

    def findMedian(self) -> float:
        if(self.len_min_heap < self.len_max_heap):
            return(-self.max_heap_for_small_nums[0])
        elif(self.len_max_heap == 0):
            return(0)
        else:
            return((self.min_heap_for_large_nums[0]-self.max_heap_for_small_nums[0])/2)
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()