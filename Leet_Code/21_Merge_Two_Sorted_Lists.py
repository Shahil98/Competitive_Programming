# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(-999999)
        new_list = head
        while(l1!=None and l2!=None):
            if(l1.val>l2.val):
                new_list.val = l2.val
                l2 = l2.next
            else:
                new_list.val = l1.val
                l1 = l1.next
            new_list_node = ListNode(-999999)
            new_list.next = new_list_node
            new_list = new_list.next
        if(l1==None):
            while(l2!=None):
                new_list.val = l2.val
                new_list.next = ListNode(-999999)
                new_list = new_list.next
                l2 = l2.next
        elif(l2==None):
            while(l1!=None):
                new_list.val = l1.val
                new_list.next = ListNode(-999999)
                new_list = new_list.next
                l1= l1.next
        new_head = head
        if(head.next == None):
            return(l1)
        while(head.next.val != -999999): 
            head = head.next
        head.next = None
        return(new_head)
        
        