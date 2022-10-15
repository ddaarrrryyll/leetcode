class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        # DP top down
        # i to keep track of curr, j is previous chosen char
        @functools.lru_cache(None)
        def soln(i, j, k, count):
            
            # base cases
            if k < 0: return inf
            if i >= len(s): return 0
        
            # if curr char is previous chosen one, we have to increment, and add 1 if curr is 1,9,or 99
            if 0 <= j < len(s) and s[i] == s[j]:
                return int(count == 1 or count == 9 or count == 99) + soln(i+1, i, k, count+1)
            
            # if new char we find the min of chosing it or not choosing it (decrement k)
            return min(1 + soln(i+1, i, k, 1), soln(i+1, j, k-1, count))
            
        return soln(0, -1, k, 0)