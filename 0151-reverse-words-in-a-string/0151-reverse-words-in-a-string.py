class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split()
        reversed_list = words[::-1]
        return " ".join(reversed_list)
        