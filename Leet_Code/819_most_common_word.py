class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned_dictionary = {}
        for word in banned:
            banned_dictionary[word] = 1
        
        word = ""
        count_dict = {}
        
        for i in range(len(paragraph)):
            if(paragraph[i].isalpha()):
                word += paragraph[i]
            elif(word!=""):
                
                word = word.lower()
                
                if(word not in count_dict):
                    count_dict[word] = 1
                else:
                    count_dict[word] += 1
                    
                word = ""
        if(word!=""):
            word = word.lower()
            if(word not in count_dict):
                count_dict[word] = 1
            else:
                count_dict[word] += 1
        ans = ""
        max_count = float("-inf")
        
        for key in count_dict:
            if(count_dict[key] > max_count and key not in banned_dictionary):
                max_count = count_dict[key]
                ans = key
        return(ans)