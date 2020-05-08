class Node():
    def __init__(self):
        self.val = ""
        self.children = []
        self.completeWord = False
class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        i = 0
        temp = 0
        while(i<len(word) and len(node.children)>0):
            temp = 0
            for child in node.children:
                if(child.val == word[i]):
                    node = child
                    i += 1
                    temp = 1
                    break
            if(temp == 0):
                break
        while(i<len(word)):
            new_node = Node()
            new_node.val = word[i]
            i += 1
            node.children.append(new_node)
            node = new_node
        node.completeWord = True
            

    def search(self, word):
        temp = 0
        i = 0
        node = self.root
        while(i<len(word)):
            if(len(node.children)<=0):
                return(False)
            temp = 0
            for child in node.children:
                if(child.val == word[i]):
                    temp = 1
                    node = child
                    break
            if(temp == 0):
                return(False)
            i += 1
        if(node.completeWord == True):
            return(True)
        else:
            return(False)

    def startsWith(self, prefix):
        i = 0
        temp = 0
        node = self.root
        while(i<len(prefix)):
            if(len(node.children)<=0):
                return(False)
            temp = 0
            for child in node.children:
                if(child.val == prefix[i]):
                    node = child
                    i += 1
                    temp = 1
                    break
            if(temp == 0):
                return(False)
            
        return(True)
        