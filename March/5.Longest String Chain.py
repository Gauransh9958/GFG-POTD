class Solution:
    def longestStrChain(self, words):
        words.sort(key=len)
        
        dp = {}
        longest_chain = 1
        
        for word in words:
            dp[word] = 1
            
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            
            longest_chain = max(longest_chain, dp[word])
        
        return longest_chain

