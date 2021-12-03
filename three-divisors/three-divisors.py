class Solution:
    def isThree(self, n: int) -> bool:
        out = 1
        for div in range(2, n+1):
            if n % div == 0:
                out += 1
                if out > 3:
                    return False
        
        return out == 3
        