class Solution:
    def countSubstrings(self, s: str) -> int:
        # counting every substring that accomodates every element as the center
        ans = 0
        for i in range(len(s)):
            ans += self.helper(i, i ,s)
            ans += self.helper(i, i+1, s)
        return ans
        
    def helper(self, i, j, s):
        # starting from first element (for odd length) / first two elements (for even length), want to find number of substrings with it in the middle
        count = 0
        # checking for palindrome
        while i >= 0 and j < len(s) and s[i] == s[j]:
            count += 1
            i -= 1
            j += 1
            
        return count
        