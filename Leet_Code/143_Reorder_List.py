# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if(head == None or head.next == None):
            return(head)
        n = 0
        new_head = head
        while(new_head!=None):
            n += 1
            new_head = new_head.next
        mid_n = n//2
        l1_head = head
        l2 = head
        while(mid_n != 0):
            if(mid_n == 1):
                pre = l2
            l2 = l2.next
            mid_n -= 1
        if(n%2 != 0):
            pre = pre.next
            l2 = l2.next
        pre.next = None
        if(l2.next != None):
            cur = l2.next
            prev = l2
            l2.next = None
            while(cur != None):
                next_ = cur.next
                cur.next = prev
                prev = cur
                cur = next_
            l2_head = prev
        else:
            l2_head = l2
        while(l1_head!= None):
            if(l2_head == None):
                l1_head.next = None
                break
            l1_next = l1_head.next
            l2_next = l2_head.next
            l1_head.next = l2_head
            l2_head.next = l1_next
            l1_head = l1_next
            l2_head = l2_next
        return(head)
            