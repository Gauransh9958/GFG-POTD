class Solution:
    def countgroup(self, arr):
        MOD = 10**9 + 7
        
        total_xor = 0
        for num in arr:
            total_xor ^= num
            
        if total_xor != 0:
            return 0
        
        frequency = {}
        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        ways = 1
        for count in frequency.values():
            
            ways = (ways * pow(2, count - 1, MOD)) % MOD
            
        return ways

