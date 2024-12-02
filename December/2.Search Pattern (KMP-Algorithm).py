class Solution:
    def search(self, pat, txt):
        res = []
        pat_len = len(pat)
        txt_len = len(txt)
        
        for i in range(txt_len - pat_len + 1):
            if txt[i:i + pat_len] == pat:
                res.append(i)
        
        return res