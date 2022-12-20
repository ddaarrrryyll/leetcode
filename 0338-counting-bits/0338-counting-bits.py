class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            # current i is the same as itself divided by 2, and if it is odd, we add 1 because when you shift left you lose a 1 lsb
            res.append(res[i>>1] + i%2)
        return res