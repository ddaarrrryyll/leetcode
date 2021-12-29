class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1: return ""
        
        # if len(palindrome) % 2 == 1:
        #   left, right = len(palindrome) // 2 - 1, len(palindrome) // 2 + 1
        # else:
        #   left, right = len(palindrome) // 2 - 1, len(palindrome) // 2
        
        palindrome = list(palindrome)
        head, tail = 0, len(palindrome) - 1
        
        while head < tail:
            if palindrome[head] != 'a':
                palindrome[head] = 'a'
                break
            head += 1
            tail -= 1
        else:
            palindrome[-1] = 'b'
            
        return "".join(palindrome)