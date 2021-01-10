# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def preorder_serialize(self, root):
        if(root == None):
            self.bst_string += " null"
        else:
            self.bst_string = self.bst_string + " " + str(root.val)
            self.preorder_serialize(root.left)
            self.preorder_serialize(root.right)
    
    def deserialize_preorder(self):
        self.count += 1
        if(self.bst_string[self.count]=="null"):
            return(None)
        else:
            node = TreeNode(int(self.bst_string[self.count]))
            node.left = self.deserialize_preorder()
            node.right = self.deserialize_preorder()
            return(node)
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.bst_string = ""
        self.preorder_serialize(root)
        return(self.bst_string)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.bst_string = data.split(" ")
        self.bst_string.pop(0)
        self.count = -1
        return(self.deserialize_preorder())

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans