"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dict_nodes = {}
        
        if(head==None):
            return(None)
        
        cur_node = head
        new_node = Node(cur_node.val, None, None)
    
        dict_nodes[cur_node] = new_node
        
        while(cur_node != None):
            if(cur_node.next==None):
                new_node.next=None
            else:
                new_node.next = Node(cur_node.next.val, None, None)
            new_node = new_node.next
            cur_node = cur_node.next
            
            dict_nodes[cur_node] = new_node
        
        cur_node = head
        
        while(cur_node != None):
            cur_new_node = dict_nodes[cur_node]
            cur_new_node.random = dict_nodes[cur_node.random]
            cur_node = cur_node.next
        return(dict_nodes[head])
        
        