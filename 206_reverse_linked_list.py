# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if(head == None or head.next==None):
            return(head)
        
        cur_node = head
        next_node = head.next
        future_node = next_node.next
        cur_node.next = None
        
        while(True):
            
            next_node.next = cur_node
            cur_node = next_node
            next_node = future_node
            if(next_node == None):
                break
            future_node = next_node.next
        
        return(cur_node)