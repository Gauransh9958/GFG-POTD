class Solution:
    def wordBreak(self, s, dictionary):
        word_set = set(dictionary)
        
        max_word_length = max(len(word) for word in dictionary)
        
        n = len(s)
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i - min(i, max_word_length), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]