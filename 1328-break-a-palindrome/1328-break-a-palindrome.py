class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        if len(palindrome) == 1:
            return ""
        
        head, tail = 0, len(palindrome)-1
        while head < tail:
            if palindrome[head] != "a":
                palindrome[head] = "a"
                return ''.join(palindrome)
            head += 1
            tail -=1
            
        palindrome[-1] = "b"
        return ''.join(palindrome)