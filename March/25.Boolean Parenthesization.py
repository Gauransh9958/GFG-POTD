class Solution:
    def countWays(self, s: str) -> int:
        dp_true = {}
        dp_false = {}
        
        def countWaysHelper(left, right):
            if (left, right) in dp_true:
                return dp_true[(left, right)], dp_false[(left, right)]
            
            if left == right:
                if s[left] == 'T':
                    return 1, 0  
                else:
                    return 0, 1  \
                
                
            true_count = 0
            false_count = 0
            
            for i in range(left + 1, right, 2):
                operator = s[i]
                left_true, left_false = countWaysHelper(left, i - 1)
                right_true, right_false = countWaysHelper(i + 1, right)
                
                if operator == '&':
                    true_count += left_true * right_true
                    false_count += left_true * right_false + left_false * right_true + left_false * right_false
                elif operator == '|':
                    true_count += left_true * right_true + left_true * right_false + left_false * right_true
                    false_count += left_false * right_false
                elif operator == '^':
                    true_count += left_true * right_false + left_false * right_true
                    false_count += left_true * right_true + left_false * right_false
            
            dp_true[(left, right)] = true_count
            dp_false[(left, right)] = false_count
            return true_count, false_count
        
        true_count, _ = countWaysHelper(0, len(s) - 1)
        return true_count
