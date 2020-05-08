# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.arr = []
        (self.dfs(root,sum,0,[]))
        return(self.arr)
    
    def dfs(self,root,sum,cur_sum,cur_arr):
        if(root == None):
            return(0)
        else:
            cur_arr.append(root.val)
            cur_sum = cur_sum + root.val
            if(cur_sum == sum and root.left==None and root.right == None):
                self.arr.append(cur_arr)
            self.dfs(root.left,sum,cur_sum,cur_arr[:])
            self.dfs(root.right,sum,cur_sum,cur_arr[:])
           
        