from collections import Counter

class Solution:
    def nonRepeatingChar(self, s):
        freq = Counter(s)
        
        for char in s:
            if freq[char] == 1:
                return char
        
        return '$'

