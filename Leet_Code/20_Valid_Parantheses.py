class Solution(object):
    def isValid(self, s):
        stack = []
        if(len(s)==0):
            return(True)
        for i in range(len(s)):
            if(s[i]=='(' or s[i]=='{' or s[i]=='['):
                stack.append(str(s[i]))
            else:
                if(len(stack)==0):
                    return(False)
                else:
                    element = stack.pop(len(stack)-1)
                    if(str(s[i])==")" and element!="("):
                        return(False)
                    elif(str(s[i])=="}" and element!="{"):
                        return(False)
                    elif(str(s[i])=="]" and element!="["):
                        return(False)    
        if(len(stack)>0):
            return(False)
        return("True")
        