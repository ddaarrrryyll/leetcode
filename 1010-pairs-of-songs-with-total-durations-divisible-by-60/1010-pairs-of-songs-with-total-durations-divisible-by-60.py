class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        def nCr(n, r):
            f = math.factorial
            return f(n) // f(r) // f(n-r)
        
        remainders = [0] * 60
        
        for song in time:
            r = song % 60
            remainders[r] += 1
        
        out = 0
        
        # any 2 will give a multiple of 6
        if remainders[0] > 1:
            out += nCr(remainders[0], 2)
            
        if remainders[30] > 1:
            out += nCr(remainders[30], 2)
        
        # need to choose the complement
        lower, upper = 1, 59
        while lower < 30 and upper > 30:
            # number of ways to choose lower * number of ways to choose upper
            out += remainders[lower] * remainders[upper]
            lower += 1
            upper -= 1
        return out
    