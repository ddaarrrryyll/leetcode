class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        score = 0
        mult = 0
        for i, c in enumerate(s):
            if c == "(":
                mult += 1
            else:
                mult -= 1
                if i > 0 and s[i-1] == "(":
                    score += 2**mult
        return score
                