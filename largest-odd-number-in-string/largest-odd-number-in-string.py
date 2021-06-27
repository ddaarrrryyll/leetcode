class Solution:
    def largestOddNumber(self, num: str) -> str:
        num = int(num)
        while num % 2 == 0 and num > 0:
            num //= 10
        
        if num == 0:
            return ""
        else:
            return str(num)
        