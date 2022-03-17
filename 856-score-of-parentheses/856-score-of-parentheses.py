class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        # counting (), smallest value is 1, which will increase exponentially
        for c in s:
            if c == "(":
                stack.append(0)
                
            else:
                v = stack.pop()
                stack[-1] += max(2*v, 1)
                
        return stack.pop()