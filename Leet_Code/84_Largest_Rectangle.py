class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = []
        
        for i in range(0, len(heights)):
            if(len(stack)==0):
                stack.append(i)
            elif(heights[stack[-1]] <= heights[i]):
                stack.append(i)
            else:
                while(stack):
                    if(heights[stack[-1]] > heights[i]):
                        cur_element = stack.pop()
                        if(stack):
                            max_area = max(max_area, (i-stack[-1]-1)*heights[cur_element])
                        else:
                            max_area = max(max_area, heights[cur_element]*i)
                    else:
                        break
                stack.append(i)
        
        while(stack):
            cur_element = stack.pop()
            if(stack):
                max_area = max(max_area, (len(heights)-stack[-1]-1)*heights[cur_element])
            else:
                max_area = max(max_area, heights[cur_element]*len(heights))
            
        
        return(max_area)