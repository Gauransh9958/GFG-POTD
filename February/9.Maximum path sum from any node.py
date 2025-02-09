
class Solution:

    def findMaxUtil(self, root):
    
        if root is None:
            return (0,float('-inf'))
    
        l, l1 = self.findMaxUtil(root.left) 
        r, r1 = self.findMaxUtil(root.right)
        
        max_single = max(max(l, r) + root.data, root.data) 
        
        max_top = max(max_single, l+r+ root.data) 
        
        res = max(max_top, l1, r1)
    
        return (max_single,res)
    
    def findMaxSum(self, root):
        
        res = self.findMaxUtil(root)
        return max(res)