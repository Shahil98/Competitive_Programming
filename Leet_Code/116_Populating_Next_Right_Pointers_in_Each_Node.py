"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if(root == None):
            return(root)
        queue = []
        queue.append(root)
        cnt = 0
        root.next = None
        while(True):
            child_arr = []
            for i in range(len(queue)):
                if(queue[i].left != None):
                    child_arr.append(queue[i].left)
                if(queue[i].right != None):
                    child_arr.append(queue[i].right)
            if(len(child_arr)==0):
                return(root)
            else:
                for i in range(len(child_arr)-1):
                    child_arr[i].next = child_arr[i+1]
                child_arr[len(child_arr)-1].next = None
            queue = child_arr
                
                