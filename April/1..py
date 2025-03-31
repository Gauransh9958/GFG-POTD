class Solution:
    def maxPartitions(self, s: str) -> int:
        last_occurrence = {char: i for i, char in enumerate(s)}
        partitions = 0
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            
            if i == end:
                partitions += 1
                start = i + 1
        
        return partitions
