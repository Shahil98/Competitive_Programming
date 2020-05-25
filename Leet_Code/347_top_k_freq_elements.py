class Solution(object):
    def __init__(self):
        self.heap_arr = []
        self.ans = []
        self.dict = {}
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            if(nums[i] not in self.dict.keys()):
                self.dict[nums[i]] = 1
            else:
                self.dict[nums[i]] += 1
                
        for key in self.dict.keys():
            self.heap_arr.append(key)
        
        self.build_heap()
        i = 0
        while(i<k):
            self.ans.append(self.heap_arr[0])
            i += 1
            self.heap_arr[0],self.heap_arr[len(self.heap_arr)-i] = self.heap_arr[len(self.heap_arr)-i],self.heap_arr[0]
            self.max_heapify(len(self.heap_arr)-i,0)
        return(self.ans)
        
    def build_heap(self):
        i = int(math.floor(len(self.heap_arr)/2)-1)
        while(i>=0):
            self.max_heapify(len(self.heap_arr),i)
            i -= 1
    def max_heapify(self,heap_size,i):
        l = (i+1)*2
        r = (i+1)*2 + 1
        if(l<=heap_size and self.dict[self.heap_arr[l-1]]>self.dict[self.heap_arr[i]]):
            largest = l-1
        else:
            largest = i
        if(r<=heap_size and self.dict[self.heap_arr[r-1]]>self.dict[self.heap_arr[largest]]):
            largest = r-1
        
        if(largest == i):
            pass
        else:
            self.heap_arr[largest],self.heap_arr[i] = self.heap_arr[i],self.heap_arr[largest]
            self.max_heapify(heap_size,largest)