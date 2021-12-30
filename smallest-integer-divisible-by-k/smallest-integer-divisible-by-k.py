class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # if k is even or if k is a multiple of 5, impossible to get 1
        if k % 2 == 0 or k % 5 == 0: return -1
        
        # 10^2 + 10^1 + 10^0
        val = 1
        # length
        length = 0
        
        while True:
            # if divisible by k
            if val % k == 0:
                return length + 1
            
            else:
                length += 1
                val = 10 * val + 1