class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        length = len(s)
        subs = []
        ans = []
        
        # function to check if string is palindrome
        def is_Palindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        # function for exploration (dfs)
        def explore(idx):
            # when we reach the end of s we append the substrings array to ans
            if idx == length:
                ans.append(subs.copy())
                return
                
            for i in range(idx, length):
                if is_Palindrome(s, idx, i):
                    subs.append(s[idx:i+1])
                    explore(i+1)
                    subs.pop()
                    
        explore(0)
        return ans