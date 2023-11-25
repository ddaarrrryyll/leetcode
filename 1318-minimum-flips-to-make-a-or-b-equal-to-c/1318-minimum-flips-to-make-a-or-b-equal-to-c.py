class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a, b, c = map(lambda x: str(bin(x))[2:][::-1], [a,b,c])
        flip = 0
        i = 0
        print()
        while i < max(len(a), len(b), len(c)):
            a_i = self.helper(a, i)
            b_i = self.helper(b, i)
            c_i = self.helper(c, i)
            
            print(a_i, b_i, c_i)
            
            if (a_i or b_i) != c_i:
                if not c_i and (a_i and b_i):
                    flip += 2
                else:
                    flip += 1
                        
            i += 1
        return flip
    
    def helper(self, x, i):
        if i >= len(x):
            return 0
        else:
            return int(x[i])