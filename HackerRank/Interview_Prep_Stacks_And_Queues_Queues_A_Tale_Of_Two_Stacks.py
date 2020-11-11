class MyQueue(object):
    
    def __init__(self):
        self.insert_stack = []
        self.remove_stack = []
    
    def peek(self):
        if(not self.remove_stack):
            while(self.insert_stack):
                self.remove_stack.append(self.insert_stack.pop())
        if(self.remove_stack):
            ele = self.remove_stack.pop()
            self.remove_stack.append(ele)
            return(ele)
        else:
            return(-1)
        
    def pop(self):
        if(not self.remove_stack):
            while(self.insert_stack):
                self.remove_stack.append(self.insert_stack.pop())
        if(self.remove_stack):
            self.remove_stack.pop()
    def put(self, value):
        self.insert_stack.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())