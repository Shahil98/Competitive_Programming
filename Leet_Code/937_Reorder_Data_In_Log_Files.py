class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digit_arr = []
        letter_arr = []
        
        for log in logs:
            log_arr = log.split(" ")
            if(not log_arr[1].isdigit()):
                letter_arr.append([log_arr[0], " ".join(log_arr[1:])])
            else:
                digit_arr.append(log)
        
        letter_arr = sorted(letter_arr, key= lambda temp:(temp[1],temp[0]))
        
        for i in range(len(letter_arr)):
            letter_arr[i] = letter_arr[i][0]+" "+letter_arr[i][1]
        return(letter_arr+digit_arr)