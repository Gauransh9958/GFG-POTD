class Solution:
    
    def areRotations(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        if s2 in s1 + s1:
            return True
        else:
            return False

