class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        for i in range(len(s)):
            if i == len(s)-1 or val[s[i]] == val[s[i+1]]:
                ans += val[s[i]]
                
            # add
            elif val[s[i]] > val[s[i+1]]:
                ans += val[s[i]]
                
            # subtract
            elif val[s[i]] < val[s[i+1]]:
                ans -= val[s[i]]
                
        return ans