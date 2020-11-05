# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if(head == None or head.next == None or m==n):
            return(head)
        
        cur_node = head
        cnt = 1
        prev_node  = None
        while(m != cnt):
            cnt += 1
            prev_node = cur_node
            cur_node = cur_node.next
    
        start_node = prev_node
        first_node = cur_node
        next_node = cur_node.next
        next_next_node = next_node.next
        while(cnt != n):
            next_node.next = cur_node
            cur_node = next_node
            next_node = next_next_node
            if(next_node == None):
                break
            next_next_node = next_node.next
            cnt += 1
        if(start_node == None):
            head = cur_node
        else:
            start_node.next = cur_node
        first_node.next = next_node
        return(head)
    
        