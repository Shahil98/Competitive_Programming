# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        temp = 0
        while(slow!=None and fast!=None):
            if(slow.next == None or fast.next == None):
                break
            if(fast.next.next == None):
                break
            if(slow.next == fast.next.next):
                temp = 1
                collision = slow.next
                break
            else:
                slow = slow.next
                fast = fast.next.next
        if(temp==1):
            while(head!=collision):
                head = head.next
                collision = collision.next
            return(collision)
        return(None)