class Solution:
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        self.valid_IP_list = []
        len_s = len(s)
        self.backtrack("",s,len_s,0)
        for i in range(len(self.valid_IP_list)):
            self.valid_IP_list[i] = self.valid_IP_list[i][:len_s+3]
        return(self.valid_IP_list)
    def backtrack(self,cur_ip,cur_str,len_s,count):
        
        if(len_s==0 and count == 4):
            self.valid_IP_list.append(cur_ip)
        elif(count>=4 or len_s==0):
            pass
        else:
            string_1 = cur_str[:1]
            self.backtrack(cur_ip+string_1+".",cur_str[1:],len_s-1,count+1)
            
            if(len_s>=3):
                string_3 = cur_str[:3]
                if(string_3[0]!='0'):
                    if(int(string_3)>=0 and int(string_3)<=255):
                        self.backtrack(cur_ip+string_3+".",cur_str[3:],len_s-3,count+1)
                
                string_2 = cur_str[:2]
                if(string_2[0]!='0'):
                    self.backtrack(cur_ip+string_2+".",cur_str[2:],len_s-2,count+1)
                    
            elif(len_s>=2):
                string_2 = cur_str[:2]
                if(string_2[0]!='0'):
                    self.backtrack(cur_ip+string_2+".",cur_str[2:],len_s-2,count+1)
        return(0)