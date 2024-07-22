class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        s = len(flowerbed)
        extended = [0] + flowerbed + [0]
        
        for i in range(1, s+1):
            if extended[i] == extended[i-1] == extended[i+1] == 0:
                extended[i] = 1
                n -= 1
            
            if n <= 0: return True
        
        return False
            