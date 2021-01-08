class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.list = []
        self.n = n
        for i in range(1, 10):
            self.recurse(i)
        return(self.list)
        
    def recurse(self, num):
        if(num <= self.n):
            self.list.append(num)
            for i in range(10):
                self.recurse(num*10+i)
        