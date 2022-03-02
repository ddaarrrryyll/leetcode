class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        
        s_split = list(s)
        s_copy = s_split.copy()
        
        for char in t:
            if char == s_copy[0]:
                print(f"{char=} {s_copy[0]=}")
                s_copy.pop(0)
                if not s_copy:
                    return True
            
            elif char not in s_copy or (char in s_copy and char != s_copy[0]):
                continue
                
            else:
                s_copy = s_split.copy()
                
        return False