class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dict_ = {}
        while(True):
            st_num = str(n)
            if(st_num in dict_.keys()):
                return(False)
            else:
                dict_[st_num] = 1
            sum = 0
            for i in range(len(st_num)):
                sum = sum + int(st_num[i])**2
            n = sum
            if(n==1):
                return(True)
        