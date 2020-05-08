# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None or head.next==None):
            return(head)
        else:
            f_cur = head
            s_cur = head.next
            temp = s_cur.next
            s_cur.next = f_cur
            f_cur.next = temp
            head = s_cur
            c = 0
            while(f_cur.next!=None and f_cur.next.next!=None):
                c = c + 1
                s_cur = f_cur.next
                t_cur = s_cur.next
                f_cur.next = t_cur
                temp = t_cur.next
                t_cur.next = s_cur
                s_cur.next = temp
                print(s_cur.val,s_cur.next)
                f_cur = s_cur
        return(head)