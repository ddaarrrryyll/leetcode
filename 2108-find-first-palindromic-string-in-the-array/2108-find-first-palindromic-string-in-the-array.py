class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""
    
    def isPalindrome(self, word):
        if word == word[::-1]:
            return True
        return False