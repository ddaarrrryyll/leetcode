class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0: return 0
        
        dp = [0 for _ in range(len(s)+1)]
        
        dp[0], dp[1] = 1, 1
        
        for i in range(2, len(s)+1):
            # take previous count since this increase in length is not counted
            if int(s[i-1:i]) > 0:
                dp[i] = dp[i-1]
                
            # new way to decode
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
                
        return dp[-1]