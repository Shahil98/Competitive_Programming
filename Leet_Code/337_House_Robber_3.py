class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return(self.cal_max(root,0))
    
    def cal_max(self,root,par):
        if(root == None):
            return(0)
        else:
            if(par == 0):
                return(max(root.val+self.cal_max(root.left,1) + self.cal_max(root.right,1),self.cal_max(root.left,0) + self.cal_max(root.right,0)))
            if(par == 1):
                return(self.cal_max(root.left,0) + self.cal_max(root.right,0))