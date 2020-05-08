class Solution(object):
    def __init__(self):
        self.dict_ = {}
        self.dict_['2'] = ["a","b","c"] 
        self.dict_['3'] = ['d','e','f']
        self.dict_['4'] = ['g','h','i']
        self.dict_['5'] = ['j','k','l']
        self.dict_['6'] = ['m','n','o']
        self.dict_['7'] = ['p','q','r','s']
        self.dict_['8'] = ['t','u','v']
        self.dict_['9'] = ['w','x','y','z']
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = self.cal_comb(digits)
        print(ans)
        return(ans)
    def cal_comb(self,s):
        if(len(s)==0):
            return([])
        if(len(s)==1):
            return(self.dict_[s])
        else:
            if(s in self.dict_.keys()):
                return(self.dict_[s])
            else:
                mid = int(math.floor(len(s)/2))
                ans1 = self.cal_comb(s[0:mid])
                ans2 = self.cal_comb(s[mid:])
                answer = []
                for i in range(len(ans1)):
                    for j in range(len(ans2)):
                        answer.append(ans1[i]+ans2[j])
                self.dict_[s] = answer
                return(answer)
            