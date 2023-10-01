class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1, p2 = 0, 1
        max_len = 0
        while p1 < p2 and p2 <= len(s):
            if len(set(s[p1:p2])) < p2-p1:
                p1+=1
            else:
                max_len = max(max_len, p2-p1)
                p2+=1
        return max_len