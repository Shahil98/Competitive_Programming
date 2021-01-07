class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        self.stones = stones
        self.dict_positions = {}
        
        self.visited = {}
        
        for i in range(len(self.stones)):
            self.dict_positions[self.stones[i]] = i
        
        return(self.recurse(0, 0))
        
    def recurse(self, position, k):
        
        if((position, k) in self.visited):
            return(self.visited[(position, k)])
        
        if(position == (len(self.stones)-1)):
            return(True)
        else:
            jump_1 = k-1
            jump_2 = k+1
            jump_3 = k
            
            ans1 = False
            ans2 = False
            ans3 = False
            
            if((self.stones[position]+jump_1) in self.dict_positions and jump_1>0):
                
                new_coordinate = self.stones[position]+jump_1
                if(self.dict_positions[new_coordinate] > position):
                    ans1 = self.recurse(self.dict_positions[new_coordinate], jump_1)
            if((self.stones[position]+jump_2) in self.dict_positions):
                
                new_coordinate = self.stones[position]+jump_2
                if(self.dict_positions[new_coordinate] > position):
                    ans2 = self.recurse(self.dict_positions[new_coordinate], jump_2)
            if((self.stones[position]+jump_3) in self.dict_positions and jump_3>0):
                
                new_coordinate = self.stones[position]+jump_3
                if(self.dict_positions[new_coordinate] > position):
                    ans3 = self.recurse(self.dict_positions[new_coordinate], jump_3)
            
            self.visited[(position, k)] = ans1 or ans2 or ans3
            return(ans1 or ans2 or ans3)
            