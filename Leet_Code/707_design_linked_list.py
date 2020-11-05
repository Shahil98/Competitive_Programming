class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.n = 0
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if(index>=self.n or index<0):
            return(-1)
        else:
            if(index == 0):
                return(self.head.val)
            cur_node = self.head
            for i in range(1,index+1):
                cur_node = cur_node.next
            return(cur_node.val)
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if(self.n == 0):
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        self.n += 1
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if(self.head == None):
            self.head = Node(val)
        else:
            cur_node = self.head
            while(cur_node.next != None):
                cur_node = cur_node.next
            last_node = Node(val)
            cur_node.next = last_node
        self.n += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if(index == 0):
            self.addAtHead(val)
        elif(index == self.n):
            self.addAtTail(val)
        elif(index<self.n):
            cnt = 0
            cur_node = self.head
            while(cnt != index):
                cnt += 1
                prev_node = cur_node
                cur_node = cur_node.next
            new_node = Node(val)
            prev_node.next = new_node
            new_node.next = cur_node
            self.n += 1
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if((index)<self.n and index>=0):
            cnt = 0
            prev_node = None
            cur_node = self.head
            while(cnt != index):
                cnt+= 1
                prev_node = cur_node
                cur_node = cur_node.next
            if(prev_node == None):
                self.head = self.head.next
            else:
                if(cur_node != None):
                    prev_node.next = cur_node.next
                else:
                    
                    prev_node.next = None
            self.n -= 1
        else:
            return(-1)
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)