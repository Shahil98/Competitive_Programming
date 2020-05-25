# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return(self.dfs(root,sum,0))
    
    def dfs(self,root,sum,cur_sum):
        if(root == None):
            return(False)
        else:
            cur_sum = cur_sum + root.val
            if(cur_sum == sum and root.left==None and root.right == None):
                return(True)
            else:
                return(self.dfs(root.left,sum,cur_sum) or self.dfs(root.right,sum,cur_sum))