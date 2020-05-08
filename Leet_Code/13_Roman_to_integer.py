class Solution(object):
    def romanToInt(self, s):
        
        dict_ = {}
        dict_['I'] = 1
        dict_['V'] = 5
        dict_['X'] = 10
        dict_['L'] = 50
        dict_['C'] = 100
        dict_['D'] = 500
        dict_['M'] = 1000
        
        sum = 0
        temp = 0
        i = 0
        while(i<len(s)):
            if(i == (len(s)-1) and temp==0):
                sum = sum + dict_[s[i]]
            elif(temp==1 and i==(len(s)-1)):
                 pass
            elif(dict_[s[i]]<dict_[s[i+1]]):
                if(i == len(s)-2):
                    temp = 1
                sum = sum + dict_[s[i+1]] - dict_[s[i]]
                i = i + 1
            else:
                sum = sum + dict_[s[i]]
            i = i + 1
        return(sum)
        
        