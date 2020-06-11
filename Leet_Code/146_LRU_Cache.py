"""
Using python dictionaries
"""

class LRUCache:
    
    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        
    def get(self, key: int) -> int:
    
        try:
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val
            return(val)
        except:
            return(-1)
    
    def put(self, key: int, value: int) -> None:
        
        try:
            self.cache[key]
            self.cache.pop(key)
            self.cache[key] = value
        except:
            if(self.count == self.capacity):
                self.cache.pop(list(self.cache.keys())[0],None)
                self.cache[key] = value
            else:
                self.cache[key] = value
                self.count += 1


            
        

