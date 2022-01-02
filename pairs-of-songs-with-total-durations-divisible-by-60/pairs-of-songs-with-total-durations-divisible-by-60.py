class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # twosum ish
        
        # stores the number of songs according to r
        remainder_list = [0] * 60
        
        for song in time:
            # r is the remainder time of each song, need to find a corresponding r' such that r + r' = 60
            r = song % 60
            remainder_list[r] += 1
        
        # print(remainder_list[0], remainder_list[30])
        
        # let remainder_list[i] = x, corresponding be x', x * x' = number of pairs for that combination        
        # for r = 0 and r = 30, we need to xC2
        
        out = 0
        if remainder_list[0] > 1:
            out += self.nCr(remainder_list[0], 2)
            
        if remainder_list[30] > 1:
            out += self.nCr(remainder_list[30], 2)
            
        head, tail = 1, 59
        
        while head < 30 and tail > 30:
            out += remainder_list[head] * remainder_list[tail]
            head += 1
            tail -= 1
        
        return out
        
    def nCr(self, n, r):
        f = math.factorial
        return f(n) // f(r) // f(n-r)