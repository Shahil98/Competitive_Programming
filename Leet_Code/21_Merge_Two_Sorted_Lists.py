# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        newList = ListNode()
        head = newList
        while(l1 != None and l2 != None):
            if(l1.val < l2.val):
                newList.next = l1
                l1 = l1.next
                newList = newList.next
            else:
                newList.next = l2
                l2 = l2.next
                newList = newList.next
        if(l1 == None):
            newList.next = l2
        else:
            newList.next = l1
        head = head.next
        return(head)