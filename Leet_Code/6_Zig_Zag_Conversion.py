class Solution:
    
    def convert(self, s: str, numRows: int) -> str:
        
        if(s == ""):
            return("")
        
        string_matrix = []
        flag = 0
        index = 0
        n = len(s)
        while(True):
            if(flag == 0):
                arr = []
                for i in range(numRows):
                    arr.append(s[index])
                    index += 1
                    if(index == n):
                        break
                string_matrix.append(arr)
                flag = 1
            elif(flag == 1):
                for j in range(numRows-2):
                    arr = []
                    for i in range(numRows):
                        arr.append("")
                    arr[numRows-j-2] = s[index]
                    string_matrix.append(arr)
                    index += 1
                    if(index == n):
                        break
                flag = 0
            if(index == n):
                break
        len_string_matrix = len(string_matrix)
        n = len(string_matrix[len_string_matrix-1])
        while(n != numRows):
            string_matrix[len_string_matrix-1].append("")
            n += 1
        output_string = ""
        for i in range(numRows):
            for j in range(len_string_matrix):
                output_string = output_string + string_matrix[j][i]
        return(output_string)
                    
                
            