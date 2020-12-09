class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen_dict = {}
        max_substring = 0
        
        n = len(s)
        cur_len = 0
        start = 0
        
        for i in range(n):
            if(s[i] in seen_dict):
                if(cur_len > max_substring):
                    max_substring = cur_len
                cur_len = i - seen_dict[s[i]]
                for j in range(start,seen_dict[s[i]]):
                    del seen_dict[s[j]]
                start = seen_dict[s[i]]+1 
                seen_dict[s[i]] = i 
                
            else:
                cur_len += 1
                seen_dict[s[i]] = i
        if(cur_len >= max_substring):
            return(cur_len)
        else:
            return(max_substring)
        