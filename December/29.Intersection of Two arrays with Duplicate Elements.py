class Solution:
    def intersectionWithDuplicates(self, a, b):
        set_a = set(a)
        set_b = set(b)
        
        result = list(set_a & set_b)
        
        return result