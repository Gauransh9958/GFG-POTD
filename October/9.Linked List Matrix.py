
'''

class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None

'''

class Solution:
    def constructLinkedMatrix(self, mat):
        if not mat:
            return None
        
        n = len(mat)
        head = None
        current_row_head = None
        prev_row_head = None

        for i in range(n):
            prev_node = None
            for j in range(n):
                new_node = Node(mat[i][j]) # type: ignore
                
                if i == 0 and j == 0:
                    head = new_node

                if prev_node:
                    prev_node.right = new_node
                
                prev_node = new_node

                if prev_row_head:
                    prev_row_head.down = new_node
                    prev_row_head = prev_row_head.right
                
        
            prev_row_head = current_row_head = head if i == 0 else current_row_head.down
        
        return head
