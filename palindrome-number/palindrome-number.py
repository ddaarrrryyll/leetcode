class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x is negative or x ends with 0 but x not 0 return false
        if x < 0 or (x % 10 == 0 and x != 0):
            return False 
        
        # keep track of the opposite direction
        backwards = 0
        while x > backwards:
            backwards = backwards * 10 + x % 10
            x = x // 10
            
        
        # even number of digits backwards = x, odd number of digits, need to remove last digit from backwards
        return x == backwards or x == backwards // 10
            