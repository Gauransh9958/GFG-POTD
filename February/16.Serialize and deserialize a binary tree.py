class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root):
        result = []
        
        def preorder(node):
            if node is None:
                result.append('N')
                return
            result.append(str(node.data))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        
        return result
    
    def deSerialize(self, arr):
        self.index = 0
        
        def build():
            if self.index >= len(arr):
                return None
            
            val = arr[self.index]
            self.index += 1
            
            if val == 'N':
                return None
            
            node = Node(int(val))
            
            node.left = build()
            node.right = build()
            
            return node
        
        return build()
