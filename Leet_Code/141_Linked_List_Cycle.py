# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        if(head == None):
            return(False)
        while((slow.next!= None) and (fast.next!= None)):
            if(fast.next.next==None):
                return(False)
            else:
                if(slow.next.val == fast.next.next.val):
                    return(True)
                else:
                    slow = slow.next
                    fast = fast.next.next
        return(False)