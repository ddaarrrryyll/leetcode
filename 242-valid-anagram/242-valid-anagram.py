from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        
        # counter counts the number of each char
        ctr = Counter([_ for _ in s])
        # decrementing corresponding char
        for char in t:
            ctr[char] -= 1
        # True if all chars have 0 as value
        return not max(ctr.values())