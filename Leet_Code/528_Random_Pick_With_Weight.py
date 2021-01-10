import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.totalSum = 0
        
        self.sum_arr = []
        
        for i in range(len(w)):
            self.totalSum += w[i]
            self.sum_arr.append(self.totalSum)
        self.w = w
        
    def binarySearch(self,left, right, key):
        mid = left + (right-left)//2
        if(mid<0):
            return(0)
        elif(mid>(len(self.sum_arr)-1)):
            return(len(self.sum_arr)-1)
        elif(left == right):
            return(left)
        elif((self.sum_arr[mid]>key and self.sum_arr[mid-1]<key) or self.sum_arr[mid]==key ):
            return(mid)
        elif(self.sum_arr[mid]>key):
            return(self.binarySearch(left, mid-1, key))
        else:
            return(self.binarySearch(mid+1, right, key))
                
    
    def pickIndex(self):
        """
        :rtype: int
        """
        random_num = random.randint(1, self.totalSum)
        return(self.binarySearch(0, len(self.sum_arr)-1, random_num))

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()