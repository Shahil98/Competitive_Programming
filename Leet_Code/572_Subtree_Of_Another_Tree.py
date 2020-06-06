# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preOrderSequence(self,st,treeNode):
        st = "#" + str(treeNode.val)
        if(treeNode.left != None):
            st = st + self.preOrderSequence(st,treeNode.left)
        else:
            st = st + "lnull"
        if(treeNode.right != None):
            st = st + self.preOrderSequence(st,treeNode.right)
        else:
            st = st + "rnull"
        return(st)
    
    def matchSubstring(self,string1,string2):
        
        for i in range(len(string2)):
            if(string1[i] != string2[i]):
                return(False)
        return(True)
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        preorderSequence_s = self.preOrderSequence("",s)
        preorderSequence_t = self.preOrderSequence("",t)
        
        if(preorderSequence_t in preorderSequence_s):
            return(True)
        else:
            return(False)
        