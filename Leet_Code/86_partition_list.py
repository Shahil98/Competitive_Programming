# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        before = ListNode()
        after = ListNode()
        head_before = before
        head_after = after
        while(head != None):
            if(head.val < x):
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        
        head_before = head_before.next
        after.next = None
        head_after = head_after.next
        if(head_before != None and head_after!=None):
            before.next = head_after
            return(head_before)
        elif(head_before == None and head_after == None):
            return(None)
        elif(head_before == None):
            return(head_after)
        else:
            return(head_before)
            
        
        