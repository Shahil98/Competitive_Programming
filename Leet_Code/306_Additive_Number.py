class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        for i in range(int(len(num)/2)):
            for j in range(i+2, len(num)):
                num1 = num[:i+1]
                num2 = num[i+1:j]  

                if(self.isValid(num1,num2,num[j:])):
                    return(True)
        
        return(False)
        
    def isValid(self, num1, num2,num):
        
        if(len(num)==0):
            return(True)

        if((num1[0]=="0" and len(num1)>1) or (num2[0]=="0" and len(num2)>1)):
            return(False)
        
        sum = str(int(num1) + int(num2))
        if(sum == num[:len(sum)]):
            return(self.isValid(num2[:], sum, num[len(sum):]))
        else:
            return(False)
