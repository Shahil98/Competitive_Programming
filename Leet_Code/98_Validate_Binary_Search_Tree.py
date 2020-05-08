# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ans = []
        self.validate(root)
        for i in range(1,len(self.ans)):
            if(self.ans[i-1]>=self.ans[i]):
                return(False)
        return(True)
                
    def validate(self,root):
        if(root == None):
            return(0)
        else:
            self.validate(root.left)
            self.ans.append(root.val)
            self.validate(root.right)
            