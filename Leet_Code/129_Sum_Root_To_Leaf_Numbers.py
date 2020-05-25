# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.arr = []
        self.dfs(root,[])
        sum_ = 0
        for array in self.arr:
            st = ""
            for val in array:
                st = st + str(val)
            sum_ = sum_ + int(st)
        return(sum_)
    
    def dfs(self,root,arr):
        if(root == None):
            return(0)
        if(root.left == None and root.right==None):
            arr.append(root.val)
            self.arr.append(arr)
            return(0)
        else:
            arr.append(root.val)
            self.dfs(root.left,arr[:])
            self.dfs(root.right,arr[:])