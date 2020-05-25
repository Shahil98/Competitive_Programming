class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if(num == 0):
            return([0])
        if(num == 1):
            return([0,1])
        arr = [0,1]
        cur_num = 2
        while(cur_num <= num):
            power_of_2 = cur_num
            arr.append(1)
            cur_num = cur_num + 1
            while(cur_num<(power_of_2*2) and cur_num<=num):
                arr.append(1+arr[cur_num-power_of_2])
                cur_num = cur_num + 1
        print(arr)
        return(arr)