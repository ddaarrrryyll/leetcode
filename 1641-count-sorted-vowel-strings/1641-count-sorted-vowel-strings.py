class Solution:
    def countVowelStrings(self, n: int) -> int:
        """
        n = 1,  a
                e
                i
                o
                u
        n = 2,  aa, ae, ai, ao, au          
                ee, ei, eo, eu              
                ii, io, iu
                oo, ou
                uu
        n = 3,  aaa, aae, aai, aao, aau
                aee, aei, aeo, aeu
                aii, aio, aiu
                aoo, aou
                auu
                eee, eei, eeo, eeu
                ...
        n = 4, aaaa, aaae, aaai, aaao, aaau
               aaee, aaei, ...
               eeee, eeei, eeeo, eeeu
               eeii, eeio, eeiu, ...
        """ 
        # [1,1,1,1,1], [1, 2, 3, 4, 5], [1, 3, 6, 10, 15]
        
        
        dp = [1] * 5
        for _ in range(1, n):
            for i in range(1, 5):
                dp[i] = dp[i] + dp[i-1]
        
        return sum(dp)