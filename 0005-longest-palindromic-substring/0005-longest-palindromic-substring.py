class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        curr_pal = ''
        curr_len = 0
        
        for i in range(len(s)):
            # odd length
            l, r = i , i
            pal, length = self.findPalindrome(s, l, r)
            if length > curr_len:
                curr_pal = pal
                curr_len = length
            # even length
            l, r = i, i+1
            pal, length = self.findPalindrome(s, l, r)
            if length > curr_len:
                curr_pal = pal
                curr_len = length
                
            # print(curr_pal)
        
        return curr_pal
    
    def findPalindrome(self, s, l, r):
        n = len(s)
        curr_len, curr_pal = 0, 0
        while l >= 0 and r < n:
            if s[l]==s[r]:
                curr_len = r+1-l
                curr_pal = s[l:r+1]
                l-=1
                r+=1
            else:
                return curr_pal, curr_len
           
        # print(f"return {curr_pal}")
        return curr_pal, curr_len
            