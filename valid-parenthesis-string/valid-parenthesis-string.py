class Solution:
    def checkValidString(self, s: str) -> bool:
        stack, s_stack = [], []
        for i, c in enumerate(s):
            if c == "*":
                s_stack.append(i)
            elif c == "(":
                stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                elif len(s_stack)>0:
                    s_stack.pop()
                else:
                    return False
        while stack and s_stack:
            if stack[-1] < s_stack[-1]:
                stack.pop()
                s_stack.pop()
            else:
                break
        
        if stack:
            return False
        else:
            return True
            