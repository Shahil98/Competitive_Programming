# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inOrderArray = []
        self.inOrder(root)
        self.originalInOrderArray = self.inOrderArray[:]
        self.inOrderArray.sort()

        n = len(self.inOrderArray)
        for i in range(n):
            if(self.inOrderArray[i] != self.originalInOrderArray[i]):
                val2 = self.inOrderArray[i]
                val1 = self.originalInOrderArray[i]
                break
        self.swap_values(root,val1,val2,0,0)
        
    def inOrder(self,node):
        if(node.left != None):
            self.inOrder(node.left)
        self.inOrderArray.append(node.val)
        if(node.right != None):
            self.inOrder(node.right)
    
    def swap_values(self,node,val1,val2,flag1,flag2):
        if(val1 == node.val and flag1!=1):
            node.val = val2
            flag1 = 1
        elif(val2 == node.val and flag2!=1):
            node.val = val1
            flag2 = 1
        if(flag1!=1 or flag2!=1):
            if(node.left != None):
                self.swap_values(node.left,val1,val2,flag1,flag2)
            if(node.right != None):
                self.swap_values(node.right,val1,val2,flag1,flag2)
        return(0)